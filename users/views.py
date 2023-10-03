from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from users.models import Farmer, Veterinarian, User
from users.serializers import FarmerSerializer, VeterinarianSerializer
from rest_framework.permissions import IsAuthenticated
from knox.auth import TokenAuthentication
from knox.models import AuthToken
from knox.settings import CONSTANTS

def check_users_exists(validated_data):
    email = validated_data['email']
    document_number = validated_data['document_number']
    if User.objects.filter(email=email).exists():
        raise serializers.ValidationError({'response':'Ya existe un usuario registrado con este correo'})
    if User.objects.filter(document_number=document_number):
        raise serializers.ValidationError({'response':'Ya existe un usuario registrado con este número de documento'})   

def get_user_from_token(token):
        user = AuthToken.objects.get(token_key=token[:CONSTANTS.TOKEN_KEY_LENGTH])
        if not user:
            return None
        return user.user

class FarmerBasic(APIView):
    
    def post(self, request):
        serializer = FarmerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        check_users_exists(serializer.validated_data)
        self.create_farmer(serializer)
        return Response({'response': 'Te has registrado existosamente'}, status=status.HTTP_201_CREATED)
        
    def create_farmer(self, farmer_serializer):
        try:
            farmer_serializer.save()
        except:
            raise serializers.ValidationError({'response':'Ha ocurrido un error al registrarte, intentalo nuevamente más tarde'})


class FarmerAuthenticated(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        token  = request.headers['Authorization'][6:]
        farmer = get_user_from_token(token)
        if not farmer:
            return Response({'response': 'No existe un usuario con este token'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = FarmerSerializer(farmer)
        return Response(serializer.data)
    
    def patch(self, request, *args, **kwargs):
        token = request.headers['Authorization'][6:]
        farmer = get_user_from_token(token)
        if not farmer:
            return Response({'response': 'No existe un usuario con este token'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = FarmerSerializer(farmer, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
"""
    def patch(self, request, *args, **kwargs):
        token = request.headers['Authorization'][6:]
        f = get_user_from_token(token)
        farmer = Farmer.objects.get(id=f.id)
        if not farmer:
            return Response({'response': 'No existe un usuario con este token'}, status=status.HTTP_400_BAD_REQUEST)
        phone_number = request.data.get('phone_number')
        address = request.data.get('address')
        city = request.data.get('city')
        if phone_number:
            farmer.phone_number = phone_number
        if address:
            farmer.address = address
        if city:
            farmer.city = city
        try:
            farmer.save()
            print("id del farmer: ", farmer.id)
        except Exception as e:
            return Response({'response': 'Error al guardar los cambios en la base de datos'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        farmer = Farmer.objects.get(id=f.id)
        serializer = FarmerSerializer(farmer)
        return Response(serializer.data)
"""

class VeterinarianBasic(APIView):
    
    def post(self, request):
        serializer = VeterinarianSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        check_users_exists(serializer.validated_data)
        self.create_veterinarian(serializer)
        return Response({'response': 'Te has registrado existosamente'}, status=status.HTTP_201_CREATED)
        
    def create_veterinarian(self, veterinarian_serializer):
        try:
            veterinarian_serializer.save()
        except Exception as e:
            raise serializers.ValidationError({'response':'Ha ocurrido un error al registrarte, intentalo nuevamente más tarde'})
   
class VeterinarianAuthenticated(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        token  = request.headers['Authorization'][6:]
        veterinarian = get_user_from_token(token)
        if not veterinarian:
            return Response({'response': 'No existe un usuario con este token'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = VeterinarianSerializer(veterinarian)
        return Response(serializer.data)
    
    def patch(self, request, *args, **kwargs):
        token = request.headers['Authorization'][6:]
        veterinarian = get_user_from_token(token)
        if not veterinarian:
            return Response({'response': 'No existe un usuario con este token'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = VeterinarianSerializer(veterinarian, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class UserDetail(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    
    def get(self, request):
        token  = request.headers['Authorization'][6:]
        user = get_user_from_token(token)
        if not user:
            return Response({'response': 'No estás logueado'}, status=status.HTTP_400_BAD_REQUEST)
        if user.role == 'veterinarian':
            serializer = VeterinarianSerializer(user)
        else:
            serializer = FarmerSerializer(user)
        return Response(serializer.data)

