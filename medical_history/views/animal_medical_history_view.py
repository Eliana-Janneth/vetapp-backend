from helpers.views.auth_farmer_view import AuthFarmerMixin
from helpers.views.auth_vet_view import AuthVetMixin
from animals.models import Animals
from medical_history.models import MedicalHistory
from farmer_request.models import Authorization
from medical_history.serializers.medical_history import MedicalHistorySerializer, MedicalHistoryUpdateSerializer, MedicalHistoryBaseSerializer, MedicalHistoryVetSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from helpers.utils.pdf_generator import generate_medical_history_pdf

class FarmerMedicalHistory(AuthFarmerMixin, APIView):
    def get(self,request,animal_id):
        farmer = self.check_authentication(request)
        if not farmer:
            return self.handle_error_response()
        try:
            animal = Animals.objects.get(id=animal_id)
            if animal.farmer.id != farmer.id:
                return self.handle_error_response()
            medical_history = MedicalHistory.objects.filter(animal=animal)
            serializer = MedicalHistoryBaseSerializer(medical_history, many=True)
            return Response(serializer.data)
        except Animals.DoesNotExist:
            return self.handle_error_response()

class VetMedicalHistory(AuthVetMixin, APIView):
    def get(self,request,animal_id):
        try:
            vet = self.check_authentication(request)
            animal = Animals.objects.get(id=animal_id)
            authorization = Authorization.objects.get(veterinarian=vet, animal=animal)
            if authorization.animal.id != animal.id and vet.id != authorization.veterinarian.id:
                return self.handle_error_response()
            medical_history = MedicalHistory.objects.filter(animal=animal)
            serializer = MedicalHistoryVetSerializer(medical_history, context={'vet':vet.id}, many=True)
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
        
    def patch(self, request, animal_id, medical_history_id):
        vet = self.check_authentication(request)
        if not vet:
            return self.handle_error_response()
        try:
            animal = Animals.objects.get(id=animal_id)
            authorization = Authorization.objects.get(veterinarian=vet, animal=animal)
            if authorization.animal.id != animal.id and vet.id != authorization.veterinarian.id:
                return self.handle_error_response()
            medical_history = MedicalHistory.objects.get(id=medical_history_id)
            if medical_history.animal.id != animal.id:
                return self.handle_error_response()
            serializer = MedicalHistoryUpdateSerializer(medical_history, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        except (Authorization.DoesNotExist, Animals.DoesNotExist, MedicalHistory.DoesNotExist):
            return self.handle_error_response()


        
class DownloadMedicalHistory(AuthFarmerMixin, APIView):
    def get(self, request, animal_id):
        farmer = self.check_authentication(request)
        if not farmer:
            return self.handle_error_response()
        try:
            animal = Animals.objects.get(id=animal_id)
            if animal.farmer.id != farmer.id:
                return self.handle_error_response()
            medical_stories = MedicalHistory.objects.filter(animal=animal_id)
            if medical_stories.count() == 0:
                return Response({'response': 'No hay historias médicas para este animal'}, status=status.HTTP_404_NOT_FOUND)
            return generate_medical_history_pdf(medical_stories)
            
        except Animals.DoesNotExist:
            return self.handle_error_response()