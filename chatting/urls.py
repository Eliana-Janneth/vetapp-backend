from django.urls import path
from chatting.views.chat_view import FarmerChatListView, VetChatListView

urlpatterns = [
    path('farmer-chats/', FarmerChatListView.as_view(), name='farmer-chats'),
    path('vet-chats/', VetChatListView.as_view(), name='vet-chats'),
    path('farmer-chats/search/', FarmerChatListView.as_view(), name='farmer-chats-search'),
    path('vet-chats/search/', VetChatListView.as_view(), name='vet-chats-search'),
]
