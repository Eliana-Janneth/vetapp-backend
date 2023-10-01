# serializers.py
from rest_framework import serializers
from .models import Animal_Species, Animal_Race, Animals

class AnimalSpeciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal_Species
        fields = '__all__'

class AnimalRaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal_Race
        fields = '__all__'

class AnimalSerializer(serializers.ModelSerializer):
    specie = serializers.CharField(source='specie.name')
    race = serializers.CharField(source='race.name')
        #     "id": 1,
        # "specie": "Vaca",
        # "race": "Aberdeen Angus",
        # "name": "Lola",
        # "color": "Blanca",
        # "birth_date": "2023-05-27",
        # "gender": "Female",
        # "weight": "120",
        # "height": "1.5",
        # "description": "Tiene cola y hace muuu",
        # "create_time": "2023-09-18T15:16:48.503273-05:00",
        # "update_time": "2023-10-01T15:23:25.602126-05:00",
        # "farmer": 41
    class Meta:
        model = Animals
        fields = '__all__'
