from helpers.views.auth_farmer_view import AuthFarmerMixin
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.models import Farmer, Veterinarian
from users.serializers.farmer_serializer import FarmerSerializer
from users.serializers.veterinarian_serializer import VeterinarianSerializer
from rest_framework.permissions import IsAuthenticated
from knox.auth import TokenAuthentication


class UserDetail(AuthFarmerMixin, APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        token = request.headers['Authorization'][6:]
        user = self.check_authentication(token)
        if not user:
            return Response({'response': 'No estás logueado'}, status=status.HTTP_400_BAD_REQUEST)
        if user.role == 'veterinarian':
            vet = Veterinarian.objects.get(id=user.id)
            serializer = VeterinarianSerializer(vet)
        else:
            farmer = Farmer.objects.get(id=user.id)
            serializer = FarmerSerializer(farmer)
        return Response(serializer.data)
