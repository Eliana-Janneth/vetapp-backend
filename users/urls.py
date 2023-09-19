from django.urls import path
from users import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = format_suffix_patterns([
    path('farmers/', views.FarmerList.as_view()),
    path('farmers/<int:id>/', views.FarmerDetail.as_view(), name='farmer-detail'),
    path('veterinarians/', views.VeterinarianList.as_view()),
    path('veterinarians/<int:id>/', views.VeterinarianDetail.as_view(), name='veterinarian-detail'),
])
