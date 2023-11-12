from django.urls import path
from chatting.views.chat_view import FarmerChatListView, VetChatListView, VetChatSearchAPIView, FarmerChatSearchAPIView
from chatting.views.image_message_view import ImageMessageView

urlpatterns = [
    path('farmer-chats/', FarmerChatListView.as_view(), name='farmer-chats'),
    path('vet-chats/', VetChatListView.as_view(), name='vet-chats'),
    path('farmer-chats/search/', FarmerChatSearchAPIView.as_view(), name='farmer-chats-search'),
    path('vet-chats/search/', VetChatSearchAPIView.as_view(), name='vet-chats-search'),
    path('chat/message/<int:message_id>/image/', ImageMessageView.as_view(), name='chat-image'),
]
