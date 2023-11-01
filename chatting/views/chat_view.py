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
        vet = self.check_authentication(request)
        if not vet:
            return self.handle_error_response()
        name = request.query_params.get('name', '')
        chats = None
        if name:
            chats = Chat().get_chats_by_farmer_or_animal_name(vet.id, name)
        else:
            chats = Chat.objects.filter(veterinarian=vet)
        serializer = VetChatListSerializer(chats, many=True)
        return Response(serializer.data)


class FarmerChatSearchAPIView(AuthFarmerMixin, APIView):
    def get(self, request):
        farmer = self.check_authentication(request)
        if not farmer:
            return self.handle_error_response()
        name = request.query_params.get('name', '')
        chats = None
        if name:
            chats = Chat().get_chats_by_vet_or_animal_name(farmer.id, name)
        else:
            chats = Chat.objects.filter(farmer=farmer)
        serializer = FarmerChatListSerializer(chats, many=True)
        return Response(serializer.data)
