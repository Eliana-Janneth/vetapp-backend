from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from knox.auth import TokenAuthentication
from knox.models import AuthToken
from knox.settings import CONSTANTS


class AuthVetMixin:
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def check_authentication(self, request):
        token = request.headers['Authorization'][6:]
        user = AuthToken.objects.get(
            token_key=token[:CONSTANTS.TOKEN_KEY_LENGTH])
        if not user or user.user.role != 'veterinarian':
            return None
        return user.user
    
    def handle_error_response(self):
        return Response({'response': 'No encontrado'}, status=status.HTTP_404_NOT_FOUND)
