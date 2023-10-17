from helpers.views.auth_farmer_view import AuthFarmerMixin
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from animals.models import Animals
from animals.serializers.animals import AnimalSerializer, AnimalListSerializer

class AnimalsFarmer(AuthFarmerMixin, APIView):

    def get(self, request):
        farmer = self.check_authentication(request)
        if not farmer:
            return self.handle_error_response()
        animals = Animals.objects.filter(farmer=farmer.id)
        animal_serializer = AnimalSerializer(animals, many=True)
        return Response(animal_serializer.data)

    def post(self, request):
        farmer = self.check_authentication(request)
        if not farmer:
            return self.handle_error_response()
        request.data['farmer'] = farmer.id
        serializer = AnimalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class AnimalDetail(AuthFarmerMixin,APIView):

    def get(self, request, pk):
        farmer = self.check_authentication(request)
        if pk is None:
            return Response({'response': 'El ID del animal es requerido'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            animal = Animals.objects.get(id=pk)
            if animal.farmer.id != farmer.id:
                return self.handle_error_response()
            serializer = AnimalSerializer(animal)
            return Response(serializer.data)
        except Animals.DoesNotExist:    
            return self.handle_error_response()

class AnimalSearchByName(AuthFarmerMixin, APIView):
    def get(self, request):
        farmer = self.check_authentication(request)
        if not farmer:
            return self.handle_error_response()
        name = request.query_params.get('name', '')
        if name == '':
            return Response({'response': 'El nombre del animal es requerido'}, status=status.HTTP_400_BAD_REQUEST)
        animals = Animals.objects.filter(name__icontains=name, farmer=farmer.id)
        serializer = AnimalSerializer(animals, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AnimalList(AuthFarmerMixin,APIView):
    def get(self, request):
        farmer = self.check_authentication(request)
        if not farmer:
            return self.handle_error_response()
        animals = Animals.objects.filter(farmer=farmer.id)
        animal_serializer = AnimalListSerializer(animals, many=True)
        return Response(animal_serializer.data)