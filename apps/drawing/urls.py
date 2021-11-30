from django.urls import path

from .views import (DrawingListCreateAPIView,
                    DrawingRetrieveUpdateDestroyAPIView,
                    StatisticsAPIView,
                    )


urlpatterns = [
    path('drawing/', DrawingListCreateAPIView.as_view()),
    path('drawing/<drawing_pk>', DrawingRetrieveUpdateDestroyAPIView.as_view()),
    path('stats/', StatisticsAPIView.as_view()),
]
