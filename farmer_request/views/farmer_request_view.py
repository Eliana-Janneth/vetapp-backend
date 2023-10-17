from helpers.views.auth_farmer_view import AuthFarmerMixin
from helpers.views.auth_vet_view import AuthVetMixin
from rest_framework.response import Response
from rest_framework import status
from animals.models import Animals
from rest_framework.views import APIView
from farmer_request.models import Authorization, FarmerRequest
from farmer_request.serializers.farmer_request import FarmerRequestSerializer

class FarmerRequestView(AuthFarmerMixin, APIView):
    
    def post(self, request):
        farmer = self.check_authentication(request)
        if not farmer:
            return self.handle_error_response()
        animal_id = request.data['animal']
        request.data['farmer'] = farmer.id
        animal = Animals.objects.get(id=animal_id)
        if animal.farmer != farmer:
            return self.handle_error_response()
        farmer_request_serializer = FarmerRequestSerializer(data=request.data)
        if farmer_request_serializer.is_valid():
            farmer_request_serializer.save()
            return Response(farmer_request_serializer.data, status=status.HTTP_201_CREATED)
        

class GetRequestAsVet(AuthVetMixin,APIView):
    def get(self, request):
        vet = self.check_authentication(request)
        if not vet:
            return self.handle_error_response()
        requests = FarmerRequest.objects.filter(veterinarian=vet.id)
        serializer = FarmerRequestSerializer(requests, many=True)
        return Response(serializer.data)
    