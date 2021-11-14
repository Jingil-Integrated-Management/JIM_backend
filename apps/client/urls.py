from django.urls import path

from .views import (ClientListCreateAPIView,
                    ClientNameListAPIView,
                    ClientRetrieveUpdateAPIView)


urlpatterns = [
    path('client/', ClientListCreateAPIView.as_view()),
    path('client/<client_pk>', ClientRetrieveUpdateAPIView.as_view()),
    path('client/name/', ClientNameListAPIView.as_view())
]
