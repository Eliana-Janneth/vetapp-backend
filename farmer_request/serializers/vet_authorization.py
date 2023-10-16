from rest_framework import serializers
from farmer_request.models import Authorization

class VetAuthorizationSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        fields = '__all__'
        model = Authorization