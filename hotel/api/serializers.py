from rest_framework import serializers

from hotel.models import Hotel, Reservation


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'
    def to_representation(self, instance):
        self.fields['hotel'] = HotelSerializer(read_only=True)
        return  super(ReservationSerializer, self).to_representation(instance)
