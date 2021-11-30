from django.urls import path

from .views import (ClientListCreateAPIView,
                    ClientRetrieveUpdateAPIView,
                    ClientNaviListAPIView,
                    DashboardClientListAPIView,
                    )


urlpatterns = [
    path('client/', ClientListCreateAPIView.as_view()),
    path('client/<client_pk>', ClientRetrieveUpdateAPIView.as_view()),
    path('navi/', ClientNaviListAPIView.as_view()),
    path('dashboard/', DashboardClientListAPIView.as_view()),
]
