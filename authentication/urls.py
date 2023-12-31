from django.urls import path
from authentication import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = format_suffix_patterns([
    path('auth/login/', views.UserLogin.as_view(), name='auth_login'),
    path('user-validation/', views.AuthTokenValidation.as_view(), name='auth_token_validation'),
])
