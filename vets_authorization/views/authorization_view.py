from helpers.views.auth_vet_view import AuthVetMixin
from helpers.views.auth_farmer_view import AuthFarmerMixin
from rest_framework.response import Response
from rest_framework import status
from animals.models import Animals
from rest_framework.views import APIView
from vets_authorization.models import Authorization
from animals.serializers.animals import AnimalSerializer

class AuthorizedAnimals(AuthVetMixin, APIView):

    def get(self, request):
        veterinarian = self.check_authentication(request) 
        if not veterinarian:
            return Response({"error": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)
        list_authorized_animals = Authorization.objects.filter(veterinarian=veterinarian).values_list('animal', flat=True)
        authorized_animals = Animals.objects.filter(id__in=list_authorized_animals)
        serializer = AnimalSerializer(authorized_animals, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
