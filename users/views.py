from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from users.models import Farmer, Veterinarian
from users.serializers import FarmerSerializer, VeterinarianSerializer

# TODO: Quitar username, generarlo de forma automática con el correo
# TODO: Validaciones de los campos, correo válido y que los campo cumplan 
# con tipo de dato. Confirmar contraseña

class FarmerList(APIView):
    def get(self, request):
        farmers_list = Farmer.objects.all()
        serializer = FarmerSerializer(farmers_list, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FarmerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.check_farmer_exists(serializer.validated_data)
        self.create_farmer(serializer)
        return Response({'message': 'Te has registrado existosamente'}, status=status.HTTP_201_CREATED)
        
    def create_farmer(self, farmer_serializer):
        try:
            farmer_serializer.save()
        except:
            raise serializers.ValidationError({'response':'Ha ocurrido un error al registrarte, intentalo nuevamente más tarde'})
            
    def check_farmer_exists(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        document_number = validated_data['document_number']
        if Farmer.objects.filter(username=username).exists() or Farmer.objects.filter(email=email).exists():
            raise serializers.ValidationError({'response':'Ya existe un usuario registrado con este correo'})
        print(Farmer.objects.filter(document_number=document_number).exists())
        if Farmer.objects.filter(document_number=document_number):
            raise serializers.ValidationError({'response':'Ya existe un usuario registrado con este número de documento'})   
    
    

class FarmerDetail(APIView):

    def get_object(self, id):
        try:
            return Farmer.objects.get(id=id)
        except Farmer.DoesNotExist:
            raise Http404

    def get(self, request, id):
        farmer = self.get_object(id)
        serializer = FarmerSerializer(farmer)
        return Response(serializer.data)

    def put(self, request, id):
        pass

    def delete(self, request, id):
        pass


class VeterinarianList(APIView):

    def get(self, request):
        farmers_list = Veterinarian.objects.all()
        serializer = VeterinarianSerializer(farmers_list, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = VeterinarianSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(request.data, status=status.HTTP_400_BAD_REQUEST)
    
class VeterinarianDetail(APIView):

    def get_object(self, id):
        try:
            return Veterinarian.objects.get(id=id)
        except Veterinarian.DoesNotExist:
            raise Http404

    def get(self, request, id):
        veterinarian = self.get_object(id)
        serializer = VeterinarianSerializer(veterinarian)
        return Response(serializer.data)

    def put(self, request, id):
        pass

    def delete(self, request, id):
        pass