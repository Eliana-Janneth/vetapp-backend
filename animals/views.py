from animals.models import Animals
from animals.serializers import AnimalSerializer, AnimalSpecieSerializer, AnimalRaceSerializer
from rest_framework import status
from rest_framework.views import APIView
from animals.models import Animals, Animal_Race, Animal_Species
from rest_framework.response import Response

class AnimalList(APIView):
    view_name = 'animals-detail'
    def get(self, request):
        animals_list = Animals.objects.all()
        context = {'request': request}
        serializer = AnimalSerializer(animals_list, many=True, context=context)
        return Response(serializer.data)

class AnimalDetail(APIView):
    pass

class AnimalSpeciesList(APIView):
    view_name = 'animal_specie-detail'
    def get(self, request):
        animal_species_list = Animal_Species.objects.all()
        context = {'request': request}
        serializer = AnimalSpecieSerializer(animal_species_list, many=True, context=context)
        return Response(serializer.data)

class AnimalSpeciesDetail(APIView):
    pass

class AnimalRaceList(APIView):
    view_name = 'animal_race-detail'
    def get(self, request):
        animal_race_list = Animal_Race.objects.all()
        context = {'request': request}
        serializer = AnimalRaceSerializer(animal_race_list, many=True, context=context)
        return Response(serializer.data)
        

class AnimalRaceDetail(APIView):
    pass