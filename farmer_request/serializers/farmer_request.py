from rest_framework import serializers
from farmer_request.models import FarmerRequest

class FarmerRequestSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        fields = '__all__'
        model = FarmerRequest