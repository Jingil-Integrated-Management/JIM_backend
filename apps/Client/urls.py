from django.urls import path

from .views import ClientListCreateAPIView, ClientRetrieveUpdateDestroyAPIView


urlpatterns = [
    path('client/', ClientListCreateAPIView.as_view()),
    path('client/<client_pk>', ClientRetrieveUpdateDestroyAPIView.as_view())
]
