from django.urls import path
from users.views.farmer_views import FarmerBasic, FarmerAuthenticated
from users.views.vet_views import VeterinarianBasic, VeterinarianAuthenticated
from users.views.user_views import UserDetail
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = format_suffix_patterns([
    path('farmers/', FarmerBasic.as_view()),
    path('farmers/auth/', FarmerAuthenticated.as_view(), name='farmer-detail'),
    path('vets/', VeterinarianBasic.as_view()),
    path('vets/auth/', VeterinarianAuthenticated.as_view(), name='veterinarian-detail'),
    path('userinfo/', UserDetail.as_view(), name='user-info'),
])
