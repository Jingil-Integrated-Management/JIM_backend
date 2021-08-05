from django.urls import path

from .views import DivisionListCreateAPIView


urlpatterns = [
    path('division/', DivisionListCreateAPIView.as_view())
]
