from wsgiref.util import FileWrapper

from django.http import HttpResponse
from rest_framework import generics

from media.api.serializers import MusicSerializer, VideoSerializer
from media.models import Music, Video


class MusicListAPIView(generics.ListAPIView):
    serializer_class = MusicSerializer
    pagination_class = None
    def get_queryset(self):
        category = self.kwargs.get('category')
        queryset = Music.objects.filter(category=category)
        return queryset

class VideoListAPIView(generics.ListAPIView):
    serializer_class = VideoSerializer
    queryset = Video.objects.all()
    pagination_class = None
