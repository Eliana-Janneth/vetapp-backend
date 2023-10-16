from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from animals.models import  AnimalRaces
from animals.serializers.animal_races import AnimalRaceSerializer
from rest_framework.permissions import IsAuthenticated
from knox.auth import TokenAuthentication
from knox.settings import CONSTANTS

class AnimalRaceList(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    
    def get(self, request):
        animal_races = AnimalRaces.objects.all()
        serializer = AnimalRaceSerializer(animal_races, many=True)
        return Response(serializer.data)
    
class AnimalRaceBySpecie(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, specie_id):
        if specie_id is None:
            return Response({'response': 'Especie_id es un parámetro requerido'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            animal_races = AnimalRaces.objects.filter(specie=specie_id)
        except AnimalRaces.DoesNotExist:    
            return Response({'response': 'No se encontraron razas para la especie especificada'}, status=status.HTTP_404_NOT_FOUND)
        serializer = AnimalRaceSerializer(animal_races, many=True)
        return Response(serializer.data)
