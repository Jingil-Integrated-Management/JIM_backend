from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import PasswordUpdateAPIView

urlpatterns = [
    path('auth/signin/', TokenObtainPairView.as_view()),
    path('auth/refresh/', TokenRefreshView.as_view()),
    path('auth/update/', PasswordUpdateAPIView.as_view())
]
