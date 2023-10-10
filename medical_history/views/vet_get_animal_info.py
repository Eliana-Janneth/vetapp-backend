from helpers.views.auth_vet_view import AuthVetMixin
from animals.models import Animals
from vets_authorization.models import Authorization
from animals.serializers.animals import AnimalSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

class AnimalInfoVet(AuthVetMixin, APIView):
    def get(self,request,animal_id):
        vet = self.check_authentication(request)
        if not vet:
            return Response({'response': 'No tienes permiso para esto'}, status=status.HTTP_400_BAD_REQUEST)
        animal = Animals.objects.get(id=animal_id)
        try:
            authorization = Authorization.objects.get(veterinarian=vet, animal=animal)
        except Authorization.DoesNotExist:
            return Response({'response': 'No tienes permiso para esto'}, status=status.HTTP_400_BAD_REQUEST)
        if authorization.animal.id != animal.id and vet.id != authorization.veterinarian.id:
            return Response({'response': 'No tienes permiso para esto'}, status=status.HTTP_400_BAD_REQUEST)        
        serializer = AnimalSerializer(animal)
        return Response(serializer.data)