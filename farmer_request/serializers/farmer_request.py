from rest_framework import serializers
from farmer_request.models import FarmerRequest

class FarmerRequestSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = FarmerRequest

class FarmerRequestAsVetSerializer(serializers.ModelSerializer):
    
    specie_name = serializers.SerializerMethodField()
    race_name = serializers.SerializerMethodField()
    animal_name = serializers.SerializerMethodField()
    farmer_name = serializers.SerializerMethodField()

    def get_specie_name(self, obj):
        return obj.animal.specie.name if obj.animal else None

    def get_race_name(self, obj):
        return obj.animal.race.name if obj.animal else None
    
    def get_animal_name(self, obj):
        return obj.animal.name if obj.animal else None
    
    def get_farmer_name(self, obj):
        return f"{obj.farmer.first_name} {obj.farmer.last_name}" if obj.farmer else None

    class Meta:
        exclude = ('farmer', 'veterinarian', 'animal', 'status')
        model = FarmerRequest

class FarmerRequestAsFarmerSerializer(serializers.ModelSerializer):
    specie_name = serializers.SerializerMethodField()
    race_name = serializers.SerializerMethodField()
    animal_name = serializers.SerializerMethodField()
    vet_name = serializers.SerializerMethodField()

    def get_specie_name(self, obj):
        return obj.animal.specie.name if obj.animal else None

    def get_race_name(self, obj):
        return obj.animal.race.name if obj.animal else None
    
    def get_animal_name(self, obj):
        return obj.animal.name if obj.animal else None
    
    def get_vet_name(self, obj):
        return f"{obj.veterinarian.first_name} {obj.veterinarian.last_name}" if obj.veterinarian else None
    class Meta:
        exclude = ('farmer', 'veterinarian', 'animal', 'status')
        model = FarmerRequest