from farmer_request.serializers.farmer_request import FarmerRequestAsVetSerializer
from helpers.views.auth_vet_view import AuthVetMixin
from rest_framework.response import Response
from animals.models import Animals
from users.models import Veterinarian, Farmer
from chatting.models import Chat
from rest_framework.views import APIView
from farmer_request.models import FarmerRequest, Authorization
from rest_framework import status

import resend
from django.core.mail import EmailMessage, get_connection
from django.conf import settings
from django.http import JsonResponse



class VetRequestView(AuthVetMixin, APIView):

    def post(self, request, farmer_request_id):
        vet = self.check_authentication(request)
        if not vet:
            return self.handle_error_response()
        try:
            farmer_request = FarmerRequest.objects.get(id=farmer_request_id)
            vet_response = request.data.get('vet_response', False)
            if vet_response is True:
                farmer_request.status = 1
                create_response = self.create_authorization(vet.id, farmer_request.animal.id)
                self.create_chat(vet.id, farmer_request.animal.id, farmer_request.farmer.id)
            else:
                farmer_request.status = 2
            farmer_request.save()
            return create_response
        except FarmerRequest.DoesNotExist:
            return self.handle_error_response()

    def create_authorization(self, vet_id, animal_id):
        try:
            animal = Animals.objects.get(id=animal_id)
            vet = Veterinarian.objects.get(id=vet_id)
            if Authorization.objects.filter(animal=animal, veterinarian=vet).first():
                return Response({'response': 'Ya existe una autorización para este veterinario y animal'},status=status.HTTP_400_BAD_REQUEST)
            Authorization.objects.create(animal = animal, veterinarian = vet)
            return Response(status=status.HTTP_200_OK)
        except (Animals.DoesNotExist, Veterinarian.DoesNotExist):
            return self.handle_error_response()

    def create_chat(self,vet_id,animal_id,farmer_id):
        try:
            animal = Animals.objects.get(id=animal_id)
            vet = Veterinarian.objects.get(id=vet_id)
            farmer = Farmer.objects.get(id=farmer_id)
        except (Animals.DoesNotExist, Veterinarian.DoesNotExist, Farmer.DoesNotExist):
            return self.handle_error_response()
        chat = Chat.objects.filter(animal=animal, veterinarian=vet, farmer=farmer)
        if chat.exists():
            print("TODO: enviar mensaje de error")
        else:
            chat = Chat.objects.create(animal=animal, veterinarian=vet, farmer=farmer)
            return Response(status=status.HTTP_200_OK)
        

class PendingRequestAsVet(AuthVetMixin, APIView):
    def get(self, request):
        vet = self.check_authentication(request)
        if not vet:
            return self.handle_error_response()
        requests = FarmerRequest.objects.filter(veterinarian=vet.id, status=0)
        serializer = FarmerRequestAsVetSerializer(requests, many=True)
        return Response(serializer.data)
