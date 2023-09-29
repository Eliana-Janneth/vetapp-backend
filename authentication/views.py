from datetime import datetime, timedelta
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from oauth2_provider.models import AccessToken

# Create your views here.
class UserLogin(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        user = authenticate(email=email, password=password)
        if user:
            login(request, user)
            token = AccessToken.objects.get_or_create(user=user, expires=datetime.now())
            #token = Token.objects.get_or_create(user=user)
            print(token[0].token)
            return Response({'token': token[1]}, status=status.HTTP_200_OK)
        return Response({'response': 'Credenciales inválidas'}, status=status.HTTP_400_BAD_REQUEST) 

class UserLogout(APIView):
    def post(self, request):
        #request.user.auth_token.delete()
        logout(request)
        return Response({'response': 'Te has deslogueado existosamente'}, status=status.HTTP_200_OK)