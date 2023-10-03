from knox.views import LoginView as KnoxLoginView
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.contrib.auth import login

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from knox.auth import TokenAuthentication
from knox.models import AuthToken
from knox.settings import CONSTANTS

class UserLogin(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request,user)
        return super().post(request,format=None)

    def get_post_response_data(self, request, token, instance):
        data = {
            'expiry': self.format_expiry_datetime(instance.expiry),
            'token': token,
            'user':{
                'role': request.user.role,
                'name': request.user.first_name,
            }
        }
        return data
    
class AuthTokenValidation(APIView):
    def get(self, request):
        token  = request.headers['Authorization'][6:]
        AuthToken.objects.get(token_key=token[:CONSTANTS.TOKEN_KEY_LENGTH])
        return Response({'response': 'Usuario autenticado'}, status=status.HTTP_202_ACCEPTED)
    
