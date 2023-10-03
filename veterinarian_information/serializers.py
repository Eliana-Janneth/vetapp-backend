from rest_framework import serializers
from veterinarian_information.models import Academic_Information, Work_Experience


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


class WorkExperienceSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=256, required=True, error_messages={
        'required': 'Por favor, ingrese un título',
        'max_length': 'El título no puede tener más de 256 caracteres'
        })
    company = serializers.CharField(max_length=100, required=True, error_messages={
        'required': 'Por favor, ingrese una empresa',
        'max_length': 'La empresa no puede tener más de 100 caracteres'
        })
    functions = serializers.CharField(max_length=256, required=True, error_messages={
        'required': 'Por favor, ingrese sus funciones',
        'max_length': 'Las funciones no puede tener más de 256 caracteres'
        })
    start_date = serializers.IntegerField(required=True, error_messages={
        'required': 'Por favor, ingrese una fecha de inicio'
        })
    end_date = serializers.IntegerField(required=False)
    country = serializers.CharField(max_length=32, required=True, error_messages={
        'required': 'Por favor, ingrese un país',
        'max_length': 'El país no puede tener más de 32 caracteres'
        })
    currently_working = serializers.BooleanField(required=True, error_messages={
        'required': 'Por favor, ingrese si está trabajando actualmente'
        })

    class Meta:
        model = Work_Experience
        exclude = ['id', 'added_time', 'update_time']
