from rest_framework import serializers
from animals.models import AnimalSpecies

class AnimalSpeciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalSpecies
        fields = '__all__'