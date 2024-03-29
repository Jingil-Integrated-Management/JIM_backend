from django.urls import path

from .views import DivisionListCreateAPIView, DivisionRetrieveUpdateDestroyAPIView, MainDivisionListAPIView


urlpatterns = [
    path('division/', DivisionListCreateAPIView.as_view()),
    path('division/<division_pk>', DivisionRetrieveUpdateDestroyAPIView.as_view()),
    path('division/main/', MainDivisionListAPIView.as_view()),
]
