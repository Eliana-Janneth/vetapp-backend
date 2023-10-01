from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from animals.models import Animal_Species, Animal_Race, Animals
from animals.serializers import AnimalSpeciesSerializer, AnimalRaceSerializer, AnimalSerializer
from users.models import Farmer
from users.serializers import FarmerSerializer
from rest_framework.permissions import IsAuthenticated
from knox.auth import TokenAuthentication
from knox.models import AuthToken
from knox.settings import CONSTANTS


class AnimalSpeciesList(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    
    def get(self, request):
        animal_species = Animal_Species.objects.all()
        serializer = AnimalSpeciesSerializer(animal_species, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AnimalSpeciesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AnimalRaceList(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        animal_races = Animal_Race.objects.all()
        serializer = AnimalRaceSerializer(animal_races, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AnimalRaceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AnimalList(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    
    def get_farmer(self, token):
        user = AuthToken.objects.get(token_key=token[:CONSTANTS.TOKEN_KEY_LENGTH])
        if not user or not user.user.role == 'farmer':
            return None
        return user.user
    
    def check_authentication(self, request):
        if not request.headers['Authorization']:
            return Response({'response': 'No estás logueado'}, status=status.HTTP_400_BAD_REQUEST)
        token  = request.headers['Authorization'][6:]
        return self.get_farmer(token)

    def get(self, request):
        farmer = self.check_authentication(request)
        if not farmer:
            return Response({'response': 'No tienes permiso para esto'}, status=status.HTTP_400_BAD_REQUEST)
        animals = Animals.objects.filter(farmer=farmer.id)
        animal_serializer = AnimalSerializer(animals, many=True)
        return Response(animal_serializer.data)

    def post(self, request):
        farmer = self.check_authentication(request)
        if not farmer:
            return Response({'response': 'No tienes permiso para esto'}, status=status.HTTP_400_BAD_REQUEST)
        request.data['farmer'] = farmer.id
        serializer = AnimalSerializer(data=request.data)
        print(repr(serializer))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class AnimalDetail(APIView):
    def get(self, request, pk):
        try:
            animal = Animals.objects.get(pk=pk)
        except Animals.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        animal_serializer = AnimalSerializer(animal)
        race_serializer = AnimalRaceSerializer(animal.race)
        species_serializer = AnimalSpeciesSerializer(animal.specie)
        
        try:
            farmer = Farmer.objects.get(id=animal.farmer.id)
        except Farmer.DoesNotExist:
            farmer = None  # En caso de que no haya un granjero asociado
        
        # Serializa la información del granjero
        farmer_serializer = FarmerSerializer(farmer)  

        data = {
            'animal': animal_serializer.data,
            'race': race_serializer.data,
            'species': species_serializer.data,
            'farmer': farmer_serializer.data 
        }
        
        return Response(data)
    

class AnimalRaceBySpecie(APIView):

    def get(self, request, specie_id):
        if specie_id is None:
            return Response({'response': 'Especie_id es un parámetro requerido'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            animal_races = Animal_Race.objects.filter(specie=specie_id)
        except Animal_Race.DoesNotExist:    
            return Response({'response': 'No se encontraron razas para la especie especificada'}, status=status.HTTP_404_NOT_FOUND)
        serializer = AnimalRaceSerializer(animal_races, many=True)
        return Response(serializer.data)
