from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from chatting.models import Chat
from chatting.serializers.chat import FarmerChatListSerializer, VetChatListSerializer
from helpers.views.auth_farmer_view import AuthFarmerMixin
from helpers.views.auth_vet_view import AuthVetMixin


class FarmerChatListView(AuthFarmerMixin, APIView):

    def get(self, request):
        farmer = self.check_authentication(request)
        if not farmer:
            return self.handle_error_response()
        chats = Chat.objects.filter(farmer=farmer)
        serializer = FarmerChatListSerializer(chats, many=True)
        return Response(serializer.data)
    
class VetChatListView(AuthVetMixin, APIView):

    def get(self, request):
        vet = self.check_authentication(request)
        if not vet:
            return self.handle_error_response()
        chats = Chat.objects.filter(veterinarian=vet)
        serializer = VetChatListSerializer(chats, many=True)
        return Response(serializer.data)
    
class VetChatSearchAPIView(AuthVetMixin, APIView):
    def get(self, request):
        farmer_name = request.query_params.get('farmer_name', '')
        animal_name = request.query_params.get('animal_name', '')

        chats = None

        if farmer_name and animal_name:
            chats = Chat().get_chats_by_farmer_and_animal_name(farmer_name, animal_name)
        elif farmer_name:
            chats = Chat().get_chats_by_farmer_name(farmer_name)
        elif animal_name:
            chats = Chat().get_chats_by_animal_name(animal_name)
        else:
            chats = Chat.objects.all()

        serializer = VetChatListSerializer(chats, many=True)
        return Response(serializer.data)


class FarmerChatSearchAPIView(AuthFarmerMixin, APIView):
    def get(self, request):
        vet_name = request.query_params.get('vet_name', '')
        animal_name = request.query_params.get('animal_name', '')

        chats = None

        if vet_name and animal_name:
            chats = Chat().get_chats_by_vet_and_animal_name(vet_name, animal_name)
        elif vet_name:
            chats = Chat().get_chats_by_vet_name(vet_name)
        elif animal_name:
            chats = Chat().get_chats_by_animal_name(animal_name)
        else:
            chats = Chat.objects.all()

        serializer = FarmerChatListSerializer(chats, many=True)
        return Response(serializer.data)
