from helpers.views.auth_vet_view import AuthVetMixin
from helpers.views.auth_farmer_view import AuthFarmerMixin
from rest_framework.response import Response
from rest_framework import status
from users.models import Veterinarian
from veterinarian_information.models import AcademicInformation
from rest_framework.views import APIView
from veterinarian_information.serializers.academic_information import AcademicInformationSerializer

class AcademicInformationVet(AuthVetMixin, APIView):

    def get(self, request):
        veterinarian = self.check_authentication(request)
        if not veterinarian:
            return self.handle_error_response()
        try:
            academic_information = AcademicInformation.objects.filter(veterinarian=veterinarian.id)
            academic_information_serializer = AcademicInformationSerializer(academic_information, many=True)
            return Response(academic_information_serializer.data)
        except AcademicInformation.DoesNotExist:
            return Response({'response': 'No se encontraron datos académicos'}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        veterinarian = self.check_authentication(request)
        if not veterinarian:
            return self.handle_error_response()
        request.data['veterinarian'] = veterinarian.id
        academic_information_serializer = AcademicInformationSerializer(data=request.data)
        if academic_information_serializer.is_valid():
            academic_information_serializer.save()
            return Response(academic_information_serializer.data, status=status.HTTP_201_CREATED)
        return Response(academic_information_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class AcademicInformationVetList(AuthFarmerMixin, APIView):

    def get(self, request, vet_id):
        try:
            farmer = self.check_authentication(request)
            if not farmer:
                return self.handle_error_response()
            veterinarian = Veterinarian.objects.get(id=vet_id)
            academic_information = AcademicInformation.objects.filter(veterinarian=veterinarian)
            academic_information_serializer = AcademicInformationSerializer(academic_information, many=True)
            return Response(academic_information_serializer.data)
        except (Veterinarian.DoesNotExist,AcademicInformation.DoesNotExist):
            return self.handle_error_response()
    
