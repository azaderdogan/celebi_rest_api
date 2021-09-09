from rest_framework import serializers

from media.models import Music,Video

class MusicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Music
        fields = '__all__'

class VideoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Video
        fields = '__all__'