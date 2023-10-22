from helpers.views.auth_vet_view import AuthVetMixin
from rest_framework.response import Response

from rest_framework.views import APIView
from farmer_request.models import FarmerRequest, Authorization

from farmer_request.serializers.farmer_request import FarmerRequestAsVetSerializer

class VetRequestView(AuthVetMixin, APIView):
    
    def post(self, request):
        pass    


    def create_authorization(self, request, vet_id, animal_id):
        authorization = Authorization()

class PendingRequestAsVet(AuthVetMixin,APIView):
    def get(self, request):
        vet = self.check_authentication(request)
        if not vet:
            return self.handle_error_response()
        requests = FarmerRequest.objects.filter(veterinarian=vet.id, status=0)
        serializer = FarmerRequestAsVetSerializer(requests, many=True)
        return Response(serializer.data)