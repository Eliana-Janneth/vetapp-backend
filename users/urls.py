from django.urls import path
from users import views


urlpatterns = [
    path('farmers/', views.FarmerList.as_view()),
    path('veterinarians/', views.FarmerList.as_view()),
]
