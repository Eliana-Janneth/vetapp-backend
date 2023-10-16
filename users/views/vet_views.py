from helpers.views.user_view import UserMixin
from helpers.views.auth_vet_view import AuthVetMixin
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from users.serializers.veterinarian_serializer import VeterinarianSerializer
from rest_framework.permissions import IsAuthenticated
from knox.auth import TokenAuthentication


class VeterinarianBasic(UserMixin, APIView):

    def post(self, request):
        serializer = VeterinarianSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.check_users_exists(serializer.validated_data)
        self.create_veterinarian(serializer)
        return Response({'response': 'Te has registrado existosamente'}, status=status.HTTP_201_CREATED)

    def create_veterinarian(self, veterinarian_serializer):
        try:
            veterinarian_serializer.save()
        except Exception:
            raise serializers.ValidationError(
                {'response': 'Ha ocurrido un error al registrarte, intentalo nuevamente más tarde'})


class VeterinarianAuthenticated(AuthVetMixin, APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        token = request.headers['Authorization'][6:]
        veterinarian = self.check_authentication(token)
        if not veterinarian:
            return Response({'response': 'No existe un usuario con este token'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = VeterinarianSerializer(veterinarian)
        return Response(serializer.data)

    def patch(self, request, *args, **kwargs):
        token = request.headers['Authorization'][6:]
        veterinarian = self.check_farmer_authentication(token)
        if not veterinarian:
            return Response({'response': 'No existe un usuario con este token'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = VeterinarianSerializer(
            veterinarian, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
