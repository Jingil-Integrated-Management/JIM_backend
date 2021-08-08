from django.urls import path

from .views import (DrawingListCreateAPIView,
                    DrawingRetrieveUpdateDestroyAPIView, DrawingFileCreateAPIView)


urlpatterns = [
    path('drawing/', DrawingListCreateAPIView.as_view()),
    path('drawing/<drawing_pk>', DrawingRetrieveUpdateDestroyAPIView.as_view()),
    path('files/', DrawingFileCreateAPIView.as_view())
]
