from helpers.views.auth_farmer_view import AuthFarmerMixin
from helpers.views.auth_vet_view import AuthVetMixin
from animals.models import Animals
from medical_history.models import MedicalHistory
from vets_authorization.models import Authorization
from medical_history.serializers.medical_history import MedicalHistorySerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

class FarmerMedicalHistory(AuthFarmerMixin, APIView):
    def get(self,request,animal_id):
        farmer = self.check_authentication(request)
        if not farmer:
            return Response({'response': 'No tienes permiso para esto'}, status=status.HTTP_400_BAD_REQUEST)
        animal = Animals.objects.get(id=animal_id)
        if animal.farmer.id != farmer.id:
            return Response({'response': 'No tienes permiso para esto'}, status=status.HTTP_400_BAD_REQUEST)        
        medical_history = MedicalHistory.objects.filter(animal=animal)
        serializer = MedicalHistorySerializer(medical_history, many=True)
        return Response(serializer.data)



class VetMedicalHistory(AuthVetMixin, APIView):
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
        medical_history = MedicalHistory.objects.filter(animal=animal)
        serializer = MedicalHistorySerializer(medical_history, many=True)
        return Response(serializer.data)

    def post(self, request, animal_id):
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
        request.data['veterinarian'] = vet.id
        request.data['animal'] = animal_id
        serializer = MedicalHistorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)