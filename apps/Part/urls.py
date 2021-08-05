from django.urls import path

from .views import PartListCreateAPIView, PartRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('part/', PartListCreateAPIView.as_view()),
    path('part/<part_pk>', PartRetrieveUpdateDestroyAPIView.as_view())
]
