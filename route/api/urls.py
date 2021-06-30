from django.urls import path
from route.api import views

urlpatterns = [
    path('places/', views.PlaceListAPIView.as_view(), name='places'),
    path('places/<int:id>/', views.PlaceDetailAPIView.as_view(), name='place_detail'),

]
