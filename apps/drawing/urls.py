from django.urls import path

from .views import (DrawingListCreateAPIView,
                    DrawingRetrieveUpdateDestroyAPIView,
                    DashboardAPIView)


urlpatterns = [
    path('drawing/', DrawingListCreateAPIView.as_view()),
    path('drawing/<drawing_pk>', DrawingRetrieveUpdateDestroyAPIView.as_view()),
    path('dashboard/', DashboardAPIView.as_view()),
]
