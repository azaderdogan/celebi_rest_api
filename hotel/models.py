from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.

class Hotel(models.Model):
    hotel_name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    district = models.CharField(max_length=200)
    rating = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    photo = models.ImageField(upload_to='uploads')


class Reservation(models.Model):
    adult = models.IntegerField()
    room = models.IntegerField()
    entry_date = models.DateField()
    release_date = models.DateField()
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)

    @property
    def total_price(self):
        price = self.room * 120
        return  price
