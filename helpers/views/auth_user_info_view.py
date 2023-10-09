from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from knox.auth import TokenAuthentication
from knox.models import AuthToken
from knox.settings import CONSTANTS


class AuthUserMixin:
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_user_info(self, request):
        if not request.headers['Authorization']:
            return Response({'response': 'No estás logueado'}, status=status.HTTP_400_BAD_REQUEST)
        token = request.headers['Authorization'][6:]
        user = AuthToken.objects.get(
            token_key=token[:CONSTANTS.TOKEN_KEY_LENGTH])
        if not user:
            return None
        return user.user
