from django.urls import path

from .views import MusicListAPIView,VideoListAPIView
urlpatterns = [
    path('musics/<str:category>/',MusicListAPIView.as_view()),
    path('videos/',VideoListAPIView.as_view()),
]