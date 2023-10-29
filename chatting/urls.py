from django.urls import path
from chatting.views.chat_view import FarmerChatListView, VetChatListView

urlpatterns = [
    path('farmer-chats/', FarmerChatListView.as_view(), name='animals'),
    path('vet-chats/', VetChatListView.as_view(), name='animals-list'),
]
