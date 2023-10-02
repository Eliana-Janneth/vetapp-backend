from medical_history.models import Veterinary_Consultations
from medical_history.serializers import VeterinaryConsultationsSerializer
from rest_framework import status
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from knox.auth import TokenAuthentication
from knox.models import AuthToken
from knox.settings import CONSTANTS

def get_user_from_token(token):
        user = AuthToken.objects.get(token_key=token[:CONSTANTS.TOKEN_KEY_LENGTH])
        if not user:
            return None
        return user.user

# Create your views here.
class VeterinaryConsultationsAPI(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        token  = request.headers['Authorization'][6:]
        veterinarian = get_user_from_token(token)
        if not veterinarian:
            return Response({'response': 'No existe un usuario con este token'}, status=status.HTTP_400_BAD_REQUEST)
        veterinary_consultations = Veterinary_Consultations.objects.filter(veterinarian=veterinarian)
        serializer = VeterinaryConsultationsSerializer(veterinary_consultations, many=True)
        return Response(serializer.data)


    def get_vet(self, token):
        user = AuthToken.objects.get(token_key=token[:CONSTANTS.TOKEN_KEY_LENGTH])
        if not user or not user.user.role == 'veterinarian':
            return None
        return user.user
    
    def check_authentication(self, request):
        if not request.headers['Authorization']:
            return Response({'response': 'No estás logueado'}, status=status.HTTP_400_BAD_REQUEST)
        token  = request.headers['Authorization'][6:]
        return self.get_vet(token)

    def post(self, request):
        veterinarian = self.check_authentication(request)
        if not veterinarian:
            return Response({'response': 'No existe un usuario con este token'}, status=status.HTTP_400_BAD_REQUEST)
        request.data['veterinarian'] = veterinarian.id
        serializer = VeterinaryConsultationsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)