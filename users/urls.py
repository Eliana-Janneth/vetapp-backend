from django.urls import path
from users import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = format_suffix_patterns([
    path('farmers/', views.FarmerBasic.as_view()),
    path('farmers/auth/', views.FarmerAuthenticated.as_view(), name='farmer-detail'),
    path('vets/', views.VeterinarianBasic.as_view()),
    path('vets/auth/', views.VeterinarianAuthenticated.as_view(), name='veterinarian-detail'),
    path('userinfo/', views.UserDetail.as_view(), name='user-info'),
])
