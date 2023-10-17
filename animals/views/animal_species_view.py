
from rest_framework.views import APIView
from rest_framework.response import Response
from animals.models import AnimalSpecies
from animals.serializers.animal_species import AnimalSpeciesSerializer
from rest_framework.permissions import IsAuthenticated
from knox.auth import TokenAuthentication
from rest_framework import status


class AnimalSpeciesList(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    
    def get(self, request):
        try: 
            animal_species = AnimalSpecies.objects.all()
            serializer = AnimalSpeciesSerializer(animal_species, many=True)
            return Response(serializer.data)
        except AnimalSpecies.DoesNotExist:
            return Response({'response': 'No se encontraron especies'}, status=status.HTTP_404_NOT_FOUND)