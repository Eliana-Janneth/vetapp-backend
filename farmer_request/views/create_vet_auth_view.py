from helpers.views.auth_farmer_view import AuthFarmerMixin
from rest_framework.response import Response
from rest_framework import status
from animals.models import Animals
from rest_framework.views import APIView
from farmer_request.models import Authorization
from farmer_request.serializers.vet_authorization import VetAuthorizationSerializer

class Authorization(AuthFarmerMixin, APIView):

    def post(self, request):
        farmer = self.check_authentication(request)
        if not farmer:
            return Response({"error": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)
        animal_id = request.data['animal']
        animal = Animals.objects.get(id=animal_id)
        if animal.farmer != farmer:
            return Response({"error": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)
        veterinarian = request.data['veterinarian']
        authorization = Authorization.objects.create(animal=animal, veterinarian=veterinarian)
        serializer = VetAuthorizationSerializer(authorization)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
