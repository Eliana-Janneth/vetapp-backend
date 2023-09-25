from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Animal_Species, Animal_Race, Animals
from .serializers import AnimalSpeciesSerializer, AnimalRaceSerializer, AnimalSerializer

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
    