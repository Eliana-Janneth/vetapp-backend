from helpers.views.auth_farmer_view import AuthFarmerMixin
from rest_framework.views import APIView
from rest_framework.response import Response
from users.serializers.veterinarian_serializer import VeterinarianListSerializer
from users.models import Veterinarian

class AvailableVetList(AuthFarmerMixin, APIView):
    
    def get(self, request):
        farmer = self.check_authentication(request)
        if not farmer:
            return self.handle_error_response()
        veterinarians = self.get_available_veterinarians()
        veterinarian_serializer = VeterinarianListSerializer(veterinarians, many=True)
        return Response(veterinarian_serializer.data)
    
    def get_available_veterinarians(self):
        return Veterinarian.objects.filter(available=True)
   
class GetVetDetail(AuthFarmerMixin, APIView):

    def get(self, request, vet_id):
        farmer = self.check_authentication(request)
        if not farmer:
            return self.handle_error_response()
        try:
            veterinarian = Veterinarian.objects.get(id=vet_id)
            veterinarian_serializer = VeterinarianListSerializer(veterinarian)
            return Response(veterinarian_serializer.data)
        except Veterinarian.DoesNotExist:
            return self.handle_error_response()

