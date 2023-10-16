from helpers.views.user_view import UserMixin
from helpers.views.auth_farmer_view import AuthFarmerMixin
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from users.serializers.farmer_serializer import FarmerSerializer


class FarmerBasic(UserMixin, APIView):

    def post(self, request):
        serializer = FarmerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.check_users_exists(serializer.validated_data)
        self.create_farmer(serializer)
        return Response({'response': 'Te has registrado existosamente'}, status=status.HTTP_201_CREATED)

    def create_farmer(self, farmer_serializer):
        try:
            farmer_serializer.save()
        except Exception:
            raise serializers.ValidationError(
                {'response': 'Ha ocurrido un error al registrarte, intentalo nuevamente más tarde'})


class FarmerAuthenticated(AuthFarmerMixin, APIView):

    def get(self, request):
        token = request.headers['Authorization'][6:]
        farmer = self.check_authentication(token)
        if not farmer:
            return Response({'response': 'No existe un usuario con este token'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = FarmerSerializer(farmer)
        return Response(serializer.data)

    def patch(self, request):
        token = request.headers['Authorization'][6:]
        farmer = self.check_authentication(token)
        if not farmer:
            return Response({'response': 'No existe un usuario con este token'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = FarmerSerializer(farmer, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
