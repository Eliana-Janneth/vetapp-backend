from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from animals.models import Animal_Species, Animal_Race, Animals
from animals.serializers import AnimalSpeciesSerializer, AnimalRaceSerializer, AnimalSerializer
from users.models import Farmer
from users.serializers import FarmerSerializer
from rest_framework.permissions import IsAuthenticated
from knox.auth import TokenAuthentication

class AnimalSpeciesList(APIView):
    
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
    def get(self, request):
        animals = Animals.objects.all()
        serializer = AnimalSerializer(animals, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AnimalSerializer(data=request.data)
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