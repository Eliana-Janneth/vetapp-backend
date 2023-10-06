from helpers.views.auth_vet_view import AuthVetMixin
from rest_framework.response import Response
from rest_framework import status
from veterinarian_information.models import Work_Experience
from rest_framework.views import APIView
from veterinarian_information.serializers.work_experience import WorkExperienceSerializer

class WorkExperienceVet(AuthVetMixin, APIView):

    def get(self, request):
        veterinarian = self.check_authentication(request)
        if not veterinarian:
            return Response({'response': 'No tienes permiso para esto'}, status=status.HTTP_400_BAD_REQUEST)
        work_experience = Work_Experience.objects.filter(veterinarian=veterinarian.id)
        work_experience_serializer = WorkExperienceSerializer(work_experience, many=True)
        return Response(work_experience_serializer.data)

    def post(self, request):
        veterinarian = self.check_authentication(request)
        if not veterinarian:
            return Response({'response': 'No tienes permiso para esto'}, status=status.HTTP_400_BAD_REQUEST)
        request.data['veterinarian'] = veterinarian.id
        work_experience_serializer = WorkExperienceSerializer(data=request.data)
        if work_experience_serializer.is_valid():
            work_experience_serializer.save()
            return Response(work_experience_serializer.data, status=status.HTTP_201_CREATED)
        return Response(work_experience_serializer.errors, status=status.HTTP_400_BAD_REQUEST)