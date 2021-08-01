from django.urls import path

from .views import ClientListCreateAPIView, UnitListCreateAPIView


urlpatterns = [
    path('client/', ClientListCreateAPIView.as_view()),
    path('unit/', UnitListCreateAPIView.as_view())
]
