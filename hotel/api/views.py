from rest_framework import generics

from hotel.api.serializers import HotelSerializer, ReservationSerializer
from hotel.models import Hotel, Reservation


class HotelListView(generics.ListAPIView):
    serializer_class = HotelSerializer
    queryset = Hotel.objects.all()


class ReservationListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ReservationSerializer
    queryset = Reservation.objects.all()
