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
        if not request.headers['Authorization']:
            return Response({'response': 'No estás logueado'}, status=status.HTTP_400_BAD_REQUEST)
        token = request.headers['Authorization'][6:]
        return self.get_veterinarian(token)

    def get_veterinarian(self, token):
        user = AuthToken.objects.get(
            token_key=token[:CONSTANTS.TOKEN_KEY_LENGTH])
        if not user or not user.user.role == 'farmer':
            return None
        return user.user
