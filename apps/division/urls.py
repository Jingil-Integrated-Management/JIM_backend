from django.urls import path

from .views import DivisionListCreateAPIView, DivisionUpdateAPIView


urlpatterns = [
    path('division/', DivisionListCreateAPIView.as_view()),
    path('division/<division_pk>', DivisionUpdateAPIView.as_view())
]
