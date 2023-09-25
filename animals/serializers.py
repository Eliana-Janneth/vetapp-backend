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
    class Meta:
        model = Animals
        fields = '__all__'
