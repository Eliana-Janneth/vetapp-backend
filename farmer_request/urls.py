from django.urls import path
from farmer_request.views.authorization_view import AuthorizedAnimals
from farmer_request.views.create_vet_auth_view import Authorization
from farmer_request.views.farmer_request_view import FarmerRequestView, FarmerRejectedRequestView, FarmerWaitingRequestView
from farmer_request.views.vet_request_view import PendingRequestAsVet, VetRequestView
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = format_suffix_patterns([
    path('authorized-animals/', AuthorizedAnimals.as_view()),
    path('authorization/', Authorization.as_view()),
    path('request/', FarmerRequestView.as_view(), name='request'),
    path('vet-requests/', PendingRequestAsVet.as_view(), name='vet-request'),
    path('vet-requests/<int:farmer_request_id>/', VetRequestView.as_view(), name='vet-request-response'),
    path('farmer-rejected-request/', FarmerRejectedRequestView.as_view(), name='farmer-rejected-request'),
    path('farmer-waiting-request/', FarmerWaitingRequestView.as_view(), name='farmer-waiting-request'),
])
