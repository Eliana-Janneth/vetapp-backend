from rest_framework import serializers
from veterinarian_information.models import Academic_Information, Work_Experience

class AcademicInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Academic_Information
        exclude = ['id', 'added_time', 'update_time']

class WorkExperienceSerializer(serializers.ModelSerializer):
     class Meta:
            model = Work_Experience
            exclude = ['id', 'added_time', 'update_time']