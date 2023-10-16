from helpers.views.auth_vet_view import AuthVetMixin
from rest_framework.response import Response
from rest_framework import status
from veterinarian_information.models import AcademicInformation
from rest_framework.views import APIView
from veterinarian_information.serializers.academic_information import AcademicInformationSerializer

class AcademicInformationVet(AuthVetMixin, APIView):

    def get(self, request):
        veterinarian = self.check_authentication(request)
        if not veterinarian:
            return self.handle_error_response()
        academic_information = AcademicInformation.objects.filter(veterinarian=veterinarian.id)
        academic_information_serializer = AcademicInformationSerializer(academic_information, many=True)
        return Response(academic_information_serializer.data)

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
    