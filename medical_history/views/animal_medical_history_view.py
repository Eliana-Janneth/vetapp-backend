from helpers.views.auth_farmer_view import AuthFarmerMixin
from helpers.views.auth_vet_view import AuthVetMixin
from animals.models import Animals
from medical_history.models import MedicalHistory
from farmer_request.models import Authorization
from medical_history.serializers.medical_history import MedicalHistorySerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

class FarmerMedicalHistory(AuthFarmerMixin, APIView):
    def get(self,request,animal_id):
        farmer = self.check_authentication(request)
        if not farmer:
            return self.handle_error_response()
        animal = Animals.objects.get(id=animal_id)
        if animal.farmer.id != farmer.id:
            return self.handle_error_response()
        medical_history = MedicalHistory.objects.filter(animal=animal)
        serializer = MedicalHistorySerializer(medical_history, many=True)
        return Response(serializer.data)

class VetMedicalHistory(AuthVetMixin, APIView):
    def get(self,request,animal_id):
        try:
            vet = self.check_authentication(request)
            animal = Animals.objects.get(id=animal_id)
            authorization = Authorization.objects.get(veterinarian=vet, animal=animal)
            if authorization.animal.id != animal.id and vet.id != authorization.veterinarian.id:
                return self.handle_error_response()
            medical_history = MedicalHistory.objects.filter(animal=animal)
            serializer = MedicalHistorySerializer(medical_history, many=True)
            return Response(serializer.data)
        except Authorization.DoesNotExist:
            return self.handle_error_response()


    def post(self, request, animal_id):
        vet = self.check_authentication(request)
        if not vet:
            return self.handle_error_response()
        try:
            animal = Animals.objects.get(id=animal_id)
            authorization = Authorization.objects.get(veterinarian=vet, animal=animal)
            if authorization.animal.id != animal.id and vet.id != authorization.veterinarian.id:
                return self.handle_error_response()
            request.data['veterinarian'] = vet.id
            request.data['animal'] = animal_id
            serializer = MedicalHistorySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except (Authorization.DoesNotExist, Animals.DoesNotExist):
            return self.handle_error_response()
        
            