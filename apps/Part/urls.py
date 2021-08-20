from django.urls import path

from .views import (PartListCreateAPIView,
                    PartRetrieveUpdateDestroyAPIView,
                    OSPartListCreateAPIView,
                    OSPartRetrieveUpdateDestroyAPIView)

urlpatterns = [
    path('part/', PartListCreateAPIView.as_view()),
    path('part/<part_pk>', PartRetrieveUpdateDestroyAPIView.as_view()),
    path('ospart/', OSPartListCreateAPIView.as_view()),
    path('ospart/<part_pk>', OSPartRetrieveUpdateDestroyAPIView.as_view())
]
