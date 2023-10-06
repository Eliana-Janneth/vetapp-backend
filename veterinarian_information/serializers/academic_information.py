from rest_framework import serializers
from veterinarian_information.models import Academic_Information


class AcademicInformationSerializer(serializers.ModelSerializer):
    title = serializers.CharField(
        max_length=256, required=True, error_messages={
            'required': 'Por favor, ingrese un título',
            'max_length': 'El título no puede tener más de 256 caracteres'
        })
    university = serializers.CharField(
        max_length=100, required=True, error_messages={
            'required': 'Por favor, ingrese una universidad',
            'max_length': 'La universidad no puede tener más de 100 caracteres'
        })
    year = serializers.IntegerField(
        required=True, error_messages={
        'required': 'Por favor, ingrese un año'
        })
    country = serializers.CharField(max_length=32, required=True, error_messages={
        'required': 'Por favor, ingrese un país',
        'max_length': 'El país no puede tener más de 32 caracteres'
        })
    academic_degree = serializers.CharField(max_length=100, required=True, error_messages={
        'required': 'Por favor, ingrese un título académico',
        'max_length': 'El título académico no puede tener más de 100 caracteres'
        })
    currently_studying = serializers.BooleanField(required=True, error_messages={
        'required': 'Por favor, ingrese si está estudiando actualmente'
        })

    class Meta:
        model = Academic_Information
        exclude = ['id', 'added_time', 'update_time']
