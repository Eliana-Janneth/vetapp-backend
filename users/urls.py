from django.urls import path
from users import views


urlpatterns = [
    path('farmers/', views.FarmerList.as_view()),
    path('farmers/<int:id>', views.FarmerDetail.as_view()),
    path('veterinarians/', views.VeterinarianList.as_view()),
    path('veterinarians/<int:id>', views.VeterinarianDetail.as_view()),
]
