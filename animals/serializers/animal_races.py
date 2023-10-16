from rest_framework import serializers
from animals.models import AnimalRaces

class AnimalRaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalRaces
        fields = '__all__'