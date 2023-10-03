from rest_framework.response import Response
from rest_framework import status
from veterinarian_information.models import Academic_Information, Work_Experience
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from knox.auth import TokenAuthentication
from knox.models import AuthToken
from knox.settings import CONSTANTS
from veterinarian_information.serializers import AcademicInformationSerializer, WorkExperienceSerializer

def get_veterinarian(token):
        user = AuthToken.objects.get(token_key=token[:CONSTANTS.TOKEN_KEY_LENGTH])
        if not user or not user.user.role == 'veterinarian':
            return None
        return user.user

def check_authentication(request):
        if not request.headers['Authorization']:
            return Response({'response': 'No estás logueado'}, status=status.HTTP_400_BAD_REQUEST)
        token  = request.headers['Authorization'][6:]
        return get_veterinarian(token)

class AcademicInformationVet(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        veterinarian = check_authentication(request)
        if not veterinarian:
            return Response({'response': 'No tienes permiso para esto'}, status=status.HTTP_400_BAD_REQUEST)
        academic_information = Academic_Information.objects.filter(veterinarian=veterinarian.id)
        academic_information_serializer = AcademicInformationSerializer(academic_information, many=True)
        return Response(academic_information_serializer.data)

    def post(self, request):
        veterinarian = check_authentication(request)
        if not veterinarian:
            return Response({'response': 'No tienes permiso para esto'}, status=status.HTTP_400_BAD_REQUEST)
        request.data['veterinarian'] = veterinarian.id
        academic_information_serializer = AcademicInformationSerializer(data=request.data)
        if academic_information_serializer.is_valid():
            academic_information_serializer.save()
            return Response(academic_information_serializer.data, status=status.HTTP_201_CREATED)
        return Response(academic_information_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WorkExperienceVet(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        veterinarian = check_authentication(request)
        if not veterinarian:
            return Response({'response': 'No tienes permiso para esto'}, status=status.HTTP_400_BAD_REQUEST)
        work_experience = Work_Experience.objects.filter(veterinarian=veterinarian.id)
        work_experience_serializer = WorkExperienceSerializer(work_experience, many=True)
        return Response(work_experience_serializer.data)

    def post(self, request):
        veterinarian = check_authentication(request)
        if not veterinarian:
            return Response({'response': 'No tienes permiso para esto'}, status=status.HTTP_400_BAD_REQUEST)
        request.data['veterinarian'] = veterinarian.id
        work_experience_serializer = WorkExperienceSerializer(data=request.data)
        if work_experience_serializer.is_valid():
            work_experience_serializer.save()
            return Response(work_experience_serializer.data, status=status.HTTP_201_CREATED)
        return Response(work_experience_serializer.errors, status=status.HTTP_400_BAD_REQUEST)