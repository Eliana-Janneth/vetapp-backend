from rest_framework import serializers
from animals.models import Animal_Species

class AnimalSpeciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal_Species
        fields = '__all__'