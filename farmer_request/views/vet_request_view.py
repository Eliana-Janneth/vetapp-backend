from helpers.views.auth_vet_view import AuthVetMixin
from rest_framework.response import Response
from animals.models import Animals
from users.models import Veterinarian
from rest_framework.views import APIView
from farmer_request.models import FarmerRequest, Authorization
from rest_framework import status

from farmer_request.serializers.farmer_request import FarmerRequestAsVetSerializer

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
                self.create_authorization(vet.id, farmer_request.animal.id)
            else:
                farmer_request.status = 2
            farmer_request.save()
            return Response(status=status.HTTP_200_OK)                
        except FarmerRequest.DoesNotExist:
            return self.handle_error_response()


    def create_authorization(self, vet_id, animal_id):
        try: 
            animal = Animals.objects.get(id=animal_id)
            vet = Veterinarian.objects.get(id=vet_id)
            authorization = Authorization()
            authorization.animal = animal
            authorization.veterinarian = vet
            authorization.save()
        except (Animals.DoesNotExist, Veterinarian.DoesNotExist):
            return self.handle_error_response()


class PendingRequestAsVet(AuthVetMixin,APIView):
    def get(self, request):
        vet = self.check_authentication(request)
        if not vet:
            return self.handle_error_response()
        requests = FarmerRequest.objects.filter(veterinarian=vet.id, status=0)
        serializer = FarmerRequestAsVetSerializer(requests, many=True)
        return Response(serializer.data)