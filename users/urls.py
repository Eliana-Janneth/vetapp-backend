from django.urls import path
from users import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = format_suffix_patterns([
    path('farmers/', views.FarmerList.as_view()),
    path('farmers/g/', views.FarmerDetail.as_view(), name='farmer-detail'),
    path('vets/', views.VeterinarianList.as_view()),
    path('vets/<int:id>/', views.VeterinarianDetail.as_view(), name='veterinarian-detail'),
    path('userinfo/', views.UserDetail.as_view(), name='user-info'),
])
