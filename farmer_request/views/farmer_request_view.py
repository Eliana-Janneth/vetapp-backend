from helpers.views.auth_farmer_view import AuthFarmerMixin
from rest_framework.response import Response
from rest_framework import status
from animals.models import Animals
from rest_framework.views import APIView
from farmer_request.models import FarmerRequest
from farmer_request.serializers.farmer_request import FarmerRequestSerializer, FarmerRequestAsFarmerSerializer


class FarmerRequestView(AuthFarmerMixin, APIView):

    def get(self, request, request_status):
        farmer = self.check_authentication(request)
        if not farmer:
            return self.handle_error_response()
        try:
            farmer_request = FarmerRequest.objects.filter(
                farmer=farmer, status=request_status)
            farmer_request_serializer = FarmerRequestAsFarmerSerializer(
                farmer_request, many=True)
            return Response(farmer_request_serializer.data, status=status.HTTP_200_OK)
        except FarmerRequest.DoesNotExist:
            return self.handle_error_response()

    def post(self, request):
        farmer = self.check_authentication(request)
        if not farmer:
            return self.handle_error_response()
        animal_id = request.data['animal']
        request.data['farmer'] = farmer.id
        veterinarian_id = request.data['veterinarian']
        try:
            animal = Animals.objects.get(id=animal_id)
            if animal.farmer.id != farmer.id:
                return self.handle_error_response()
            farmer_request_serializer = FarmerRequestSerializer(
                data=request.data)
            farmer_request_exists = FarmerRequest.objects.filter(
                animal=animal, status=0, farmer=farmer.id, veterinarian=veterinarian_id).first()
            if farmer_request_exists:
                return Response({'response': 'Ya existe una solicitud pendiente para este animal'}, status=status.HTTP_400_BAD_REQUEST)
            if farmer_request_serializer.is_valid():
                farmer_request_serializer.save()
                return Response(farmer_request_serializer.data, status=status.HTTP_201_CREATED)
        except Animals.DoesNotExist:
            return self.handle_error_response()
