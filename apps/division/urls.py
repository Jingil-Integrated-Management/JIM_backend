from django.urls import path

from .views import DivisionListCreateAPIView, DivisionUpdateAPIView, MainDivisionListAPIView


urlpatterns = [
    path('division/', DivisionListCreateAPIView.as_view()),
    path('division/<division_pk>', DivisionUpdateAPIView.as_view()),
    path('division/main/', MainDivisionListAPIView.as_view()),
]
