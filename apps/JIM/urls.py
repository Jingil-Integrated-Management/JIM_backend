from django.urls import path

from .views import (ClientListCreateAPIView, UnitListCreateAPIView,
                    DrawingListCreateAPIView, DivisionListCreateAPIView)


urlpatterns = [
    path('client/', ClientListCreateAPIView.as_view()),
    path('unit/', UnitListCreateAPIView.as_view()),
    path('drawing/', DrawingListCreateAPIView.as_view()),
    path('division/', DivisionListCreateAPIView.as_view())
]
