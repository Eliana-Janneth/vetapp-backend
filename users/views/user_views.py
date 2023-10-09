from helpers.views.auth_user_info_view import AuthUserMixin
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.models import Farmer, Veterinarian
from users.serializers.farmer_serializer import FarmerSerializer
from users.serializers.veterinarian_serializer import VeterinarianSerializer

class UserDetail(AuthUserMixin, APIView):

    def get(self, request):
        user = self.get_user_info(request)
        if not user:
            return Response({'response': 'No estás logueado'}, status=status.HTTP_400_BAD_REQUEST)
        if user.role == 'veterinarian':
            vet = Veterinarian.objects.get(id=user.id)
            serializer = VeterinarianSerializer(vet)
        else:
            farmer = Farmer.objects.get(id=user.id)
            serializer = FarmerSerializer(farmer)
        return Response(serializer.data) 