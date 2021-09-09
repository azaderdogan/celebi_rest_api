from django.urls import path

from .views import HotelListView,ReservationListCreateAPIView
urlpatterns = [
    path('',HotelListView.as_view()),
    path('reservation/',ReservationListCreateAPIView.as_view())
]