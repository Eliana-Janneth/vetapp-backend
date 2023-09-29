from django.urls import path
from authentication import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = format_suffix_patterns([
    path('auth/login/', views.UserLogin.as_view(), name='auth_login'),
    path('auth/logout/', views.UserLogout.as_view(), name='auth_logout'),
])
