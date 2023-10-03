from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from animals.models import Animal_Species, Animal_Race, Animals
from animals.serializers import AnimalSpeciesSerializer, AnimalRaceSerializer, AnimalSerializer
from rest_framework.permissions import IsAuthenticated
from knox.auth import TokenAuthentication
from knox.models import AuthToken
from knox.settings import CONSTANTS

def get_farmer(token):
    user = AuthToken.objects.get(token_key=token[:CONSTANTS.TOKEN_KEY_LENGTH])
    if not user or not user.user.role == 'farmer':
        return None
    return user.user
 
def check_authentication(request):
    if not request.headers['Authorization']:
        return Response({'response': 'No estás logueado'}, status=status.HTTP_400_BAD_REQUEST)
    token  = request.headers['Authorization'][6:]
    return get_farmer(token)

class AnimalSpeciesList(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    
    def get(self, request):
        animal_species = Animal_Species.objects.all()
        serializer = AnimalSpeciesSerializer(animal_species, many=True)
        return Response(serializer.data)

class AnimalRaceList(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    
    def get(self, request):
        animal_races = Animal_Race.objects.all()
        serializer = AnimalRaceSerializer(animal_races, many=True)
        return Response(serializer.data)

class AnimalFarmer(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        farmer = check_authentication(request)
        if not farmer:
            return Response({'response': 'No tienes permiso para esto'}, status=status.HTTP_400_BAD_REQUEST)
        animals = Animals.objects.filter(farmer=farmer.id)
        animal_serializer = AnimalSerializer(animals, many=True)
        return Response(animal_serializer.data)

    def post(self, request):
        farmer = check_authentication(request)
        if not farmer:
            return Response({'response': 'No tienes permiso para esto'}, status=status.HTTP_400_BAD_REQUEST)
        request.data['farmer'] = farmer.id
        serializer = AnimalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class AnimalDetail(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        farmer = get_farmer(request.headers['Authorization'][6:])
        if pk is None:
            return Response({'response': 'El ID del animal es requerido'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            animal = Animals.objects.get(id=pk)
            if animal.farmer.id != farmer.id:
                return Response({'response': 'No tienes permiso para esto'}, status=status.HTTP_400_BAD_REQUEST)
        except Animals.DoesNotExist:    
            return Response({'response': 'No se encontraron razas para la especie especificada'}, status=status.HTTP_404_NOT_FOUND)
        serializer = AnimalSerializer(animal)
        return Response(serializer.data)

class AnimalRaceBySpecie(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, specie_id):
        if specie_id is None:
            return Response({'response': 'Especie_id es un parámetro requerido'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            animal_races = Animal_Race.objects.filter(specie=specie_id)
        except Animal_Race.DoesNotExist:    
            return Response({'response': 'No se encontraron razas para la especie especificada'}, status=status.HTTP_404_NOT_FOUND)
        serializer = AnimalRaceSerializer(animal_races, many=True)
        return Response(serializer.data)
