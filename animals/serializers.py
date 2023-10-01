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
    specie = serializers.PrimaryKeyRelatedField(queryset=Animal_Species.objects.all(), write_only=True)
    race = serializers.PrimaryKeyRelatedField(queryset=Animal_Race.objects.all(), write_only=True)
    specie_name = serializers.SerializerMethodField()
    race_name = serializers.SerializerMethodField()
    name=serializers.CharField(max_length=50)
    color=serializers.CharField(max_length=50)
    birth_date=serializers.DateField()
    gender=serializers.CharField(max_length=50)
    weight=serializers.CharField()
    height=serializers.CharField()
    description=serializers.CharField(max_length=50)

    class Meta:
        model = Animals
        exclude =["create_time","update_time"]
    
    def get_specie_name(self, obj):
        return obj.specie.name if obj.specie else None

    def get_race_name(self, obj):
        return obj.race.name if obj.race else None

    def validate(self, validated_data):
        specie_id = validated_data['specie'].id
        race_id = validated_data['race'].id
        try:
            race = Animal_Race.objects.get(id=race_id)
            if race.specie_id != specie_id:
                raise serializers.ValidationError({'response': 'La raza no pertenece a la especie'})
        except Animal_Race.DoesNotExist:
            raise serializers.ValidationError({'response': 'La raza especificada no existe'})
        return validated_data
    
