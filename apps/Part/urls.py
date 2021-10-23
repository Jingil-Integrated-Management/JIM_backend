from django.urls import path

from .views import (PartListCreateAPIView,
                    PartRetrieveUpdateDestroyAPIView,
                    OutSourceCreateAPIView,
                    PartFileCreateAPIView)

urlpatterns = [
    path('part/', PartListCreateAPIView.as_view()),
    path('part/<part_pk>', PartRetrieveUpdateDestroyAPIView.as_view()),
    path('outsource/', OutSourceCreateAPIView.as_view()),
    path('files/', PartFileCreateAPIView.as_view())
]
