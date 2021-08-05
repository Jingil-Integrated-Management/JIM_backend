from django.urls import path

from .views import ClientListCreateAPIView


urlpatterns = [
    path('client/', ClientListCreateAPIView.as_view())
]
