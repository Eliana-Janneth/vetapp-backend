from rest_framework import serializers
from animals.models import Animal_Race

class AnimalRaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal_Race
        fields = '__all__'