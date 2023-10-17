from helpers.views.auth_farmer_view import AuthFarmerMixin
from rest_framework.views import APIView
from rest_framework.response import Response
from users.serializers.veterinarian_serializer import VeterinarianSerializer, VeterinarianListSerializer
from users.models import Veterinarian
from veterinarian_information.models import AcademicInformation, WorkExperience   
from veterinarian_information.serializers.academic_information import AcademicInformationSerializer 
from veterinarian_information.serializers.work_experience import WorkExperienceSerializer
class AvailableVetList(AuthFarmerMixin, APIView):
    
    def get(self, request):
        farmer = self.check_authentication(request)
        if not farmer:
            return self.handle_error_response()
        veterinarians = self.get_available_veterinarians()
        veterinarian_serializer = VeterinarianListSerializer(veterinarians, many=True)
        return Response(veterinarian_serializer.data)
    
    def get_available_veterinarians(self):
        return Veterinarian.objects.filter(available=True)
   
class GetVetDetail(AuthFarmerMixin, APIView):

    def get(self, request, vet_id):
        farmer = self.check_authentication(request)
        if not farmer:
            return self.handle_error_response()
        veterinarians = Veterinarian.objects.get(id=vet_id)
        veterinarian_serializer = VeterinarianListSerializer(veterinarians)
        return Response(veterinarian_serializer.data)

class GetVetAcademicInfoList(AuthFarmerMixin, APIView):

    def get(self, request, vet_id):
        try:
            farmer = self.check_authentication(request)
            if not farmer:
                return self.handle_error_response()
            academic_information = AcademicInformation.objects.filter(veterinarian=vet_id)
            academic_information_serializer = AcademicInformationSerializer(academic_information, many=True)
            return Response(academic_information_serializer.data)
        except AcademicInformation.DoesNotExist:
            return self.handle_error_response()
    
class GetVetWorkExperienceList(AuthFarmerMixin, APIView):

    def get(self, request, vet_id):
        try:
            farmer = self.check_authentication(request)
            if not farmer:
                return self.handle_error_response()
            work_experience = WorkExperience.objects.filter(veterinarian=vet_id)
            work_experience_serializer = WorkExperienceSerializer(work_experience)
            return Response(work_experience_serializer.data)
        except WorkExperience.DoesNotExist:
            return self.handle_error_response()