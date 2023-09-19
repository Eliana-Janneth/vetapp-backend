from rest_framework import routers, serializers, viewsets
from animals.models import Animals, Animal_Race, Animal_Species


class AnimalSerializer(serializers.HyperlinkedModelSerializer):
    farmer = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='farmer-detail'
    )
    class Meta:
        model = Animals
        exclude = ['create_time','update_time']

class AnimalSpecieSerializer(serializers.HyperlinkedModelSerializer):
    animal = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='animal-detail'
    )
    class Meta:
        model = Animal_Species
        fields = '__all__'
        

class AnimalRaceSerializer(serializers.HyperlinkedModelSerializer):
    animal_specie = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='animal_specie-detail'
    )
    class Meta:
        model = Animal_Race
        fields = '__all__'