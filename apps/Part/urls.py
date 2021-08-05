from django.urls import path

from .views import PartListCreateAPIView

urlpatterns = [
    path('part/', PartListCreateAPIView.as_view())
]
