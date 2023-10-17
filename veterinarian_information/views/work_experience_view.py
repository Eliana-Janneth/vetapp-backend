from helpers.views.auth_vet_view import AuthVetMixin
from helpers.views.auth_farmer_view import AuthFarmerMixin
from rest_framework.response import Response
from rest_framework import status
from veterinarian_information.models import WorkExperience
from users.models import Veterinarian
from rest_framework.views import APIView
from veterinarian_information.serializers.work_experience import WorkExperienceSerializer

class WorkExperienceVet(AuthVetMixin, APIView):

    def get(self, request):
        veterinarian = self.check_authentication(request)
        if not veterinarian:
            return self.handle_error_response()
        try:
            work_experience = WorkExperience.objects.filter(veterinarian=veterinarian.id)
            work_experience_serializer = WorkExperienceSerializer(work_experience, many=True)
            return Response(work_experience_serializer.data)
        except WorkExperience.DoesNotExist:
            return Response({'response': 'No se encontraron datos de experiencia laboral'}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        veterinarian = self.check_authentication(request)
        if not veterinarian:
            return self.handle_error_response()
        request.data['veterinarian'] = veterinarian.id
        work_experience_serializer = WorkExperienceSerializer(data=request.data)
        if work_experience_serializer.is_valid():
            work_experience_serializer.save()
            return Response(work_experience_serializer.data, status=status.HTTP_201_CREATED)
        return Response(work_experience_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class WorkExperienceVetList(AuthFarmerMixin, APIView):

    def get(self, request, vet_id):
        try:
            farmer = self.check_authentication(request)
            if not farmer:
                return self.handle_error_response()
            veterinarian = Veterinarian.objects.get(id=vet_id)
            work_experience = WorkExperience.objects.filter(veterinarian=veterinarian)
            work_experience_serializer = WorkExperienceSerializer(work_experience, many=True)
            return Response(work_experience_serializer.data)
        except (Veterinarian.DoesNotExist, WorkExperience.DoesNotExist):
            return self.handle_error_response()