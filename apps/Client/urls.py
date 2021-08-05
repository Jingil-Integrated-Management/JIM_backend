from django.urls import path

from .views import ClientListCreateAPIView, ClientRetrieveUpdateAPIView


urlpatterns = [
    path('client/', ClientListCreateAPIView.as_view()),
    path('client/<client_pk>', ClientRetrieveUpdateAPIView.as_view())
]
