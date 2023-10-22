from rest_framework import serializers
from animals.models import AnimalSpecies, AnimalRaces, Animals


class AnimalSerializer(serializers.ModelSerializer):
    specie = serializers.PrimaryKeyRelatedField(
        required=True, queryset=AnimalSpecies.objects.all(), write_only=True, error_messages={
            'required': 'La especie del animal es requerida',
            'does_not_exist': 'La especie especificada no existe',
            'incorrect_type': 'El nombre de la especie debe ser un número entero',
        })
    race = serializers.PrimaryKeyRelatedField(
        required=True, queryset=AnimalRaces.objects.all(), write_only=True,  error_messages={
            'required': 'La raza del animal es requerida',
            'does_not_exist': 'La raza especificada no existe',
            'incorrect_type': 'El nombre de la raza debe ser un número entero',
        })
    specie_name = serializers.SerializerMethodField()
    race_name = serializers.SerializerMethodField()
    name = serializers.CharField(required=True, max_length=50, error_messages={
        'required': 'El nombre del animal es requerido',
        'max_length': 'El nombre del animal no puede tener más de 50 caracteres'
    })
    color = serializers.CharField(required=True, max_length=50, error_messages={
        'required': 'El color del animal es requerido',
        'max_length': 'El color del animal no puede tener más de 50 caracteres'
    })
    birth_date = serializers.DateField(required=True, error_messages={
        'required': 'La fecha de nacimiento del animal es requerida',
        'invalid': 'La fecha de nacimiento del animal debe tener el formato YYYY-MM-DD'
    })
    gender = serializers.CharField(required=True, max_length=10, error_messages={
        'required': 'El género del animal es requerido',
        'max_length': 'El género del animal no puede tener más de 10 caracteres'
    })
    weight = serializers.CharField(required=False, max_length=10, error_messages={
        'max_length': 'El peso del animal no puede tener más de 10 caracteres'
    })
    height = serializers.CharField(required=False, max_length=10, error_messages={
        'max_length': 'La altura del animal no puede tener más de 10 caracteres'
    })
    description = serializers.CharField(required=False, max_length=1000, error_messages={
        'max_length': 'La descripción del animal no puede tener más de 1000 caracteres'
    })

    class Meta:
        model = Animals
        exclude = ["create_time", "update_time"]

    def get_specie_name(self, obj):
        return obj.specie.name if obj.specie else None

    def get_race_name(self, obj):
        return obj.race.name if obj.race else None

    def validate(self, validated_data):
        if 'specie' in validated_data and 'race' in validated_data:
            specie_id = validated_data['specie'].id
            race_id = validated_data['race'].id
            try:
                race = AnimalRaces.objects.get(id=race_id)
                if race.specie_id != specie_id:
                    raise serializers.ValidationError(
                        {'response': 'La raza no pertenece a la especie'})
            except AnimalRaces.DoesNotExist:
                raise serializers.ValidationError(
                    {'response': 'La raza especificada no existe'})
        return validated_data


class AnimalUpdateSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=False, max_length=50, error_messages={
        'max_length': 'El nombre del animal no puede tener más de 50 caracteres'
    })
    color = serializers.CharField(required=False, max_length=50, error_messages={
        'max_length': 'El color del animal no puede tener más de 50 caracteres'
    })
    birth_date = serializers.DateField(required=False, error_messages={
        'invalid': 'La fecha de nacimiento del animal debe tener el formato YYYY-MM-DD'
    })
    weight = serializers.CharField(required=False, max_length=10, error_messages={
        'max_length': 'El peso del animal no puede tener más de 10 caracteres'
    })
    height = serializers.CharField(required=False, max_length=10, error_messages={
        'max_length': 'La altura del animal no puede tener más de 10 caracteres'
    })
    description = serializers.CharField(required=False, max_length=1000, error_messages={
        'max_length': 'La descripción del animal no puede tener más de 1000 caracteres'
    })

    class Meta:
        model = Animals
        exclude = ["create_time", "update_time", "farmer", "specie", "race", "gender"]
        read_only_fields = ["id"]


class AnimalListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animals
        fields = ["id", "name"]
