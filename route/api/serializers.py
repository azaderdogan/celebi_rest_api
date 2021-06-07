from rest_framework import serializers

from route.models import Place


class PlaceSerializer(serializers.ModelSerializer):
    geolocation = serializers.SerializerMethodField()

    class Meta:
        model = Place
        fields = ['id', 'created_at', 'name', 'description', 'country', 'geolocation']

    def get_geolocation(self, obj):
        return obj.geolocation


class TestSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    value = serializers.CharField(max_length=100)
