
from rest_framework.views import APIView
from rest_framework.response import Response
from animals.models import Animal_Species
from animals.serializers.animal_species import AnimalSpeciesSerializer
from rest_framework.permissions import IsAuthenticated
from knox.auth import TokenAuthentication


class AnimalSpeciesList(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    
    def get(self, request):
        animal_species = Animal_Species.objects.all()
        serializer = AnimalSpeciesSerializer(animal_species, many=True)
        return Response(serializer.data)