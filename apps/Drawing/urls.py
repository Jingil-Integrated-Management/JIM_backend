from django.urls import path

from .views import DrawingListCreateAPIView


urlpatterns = [
    path('drawing/', DrawingListCreateAPIView.as_view())
]
