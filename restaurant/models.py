from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.
class Restaurant(models.Model):
    restaurant_name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    district = models.CharField(max_length=200)
    rating = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    photo = models.ImageField(upload_to='uploads')

class Reservation(models.Model):
    adult = models.IntegerField()
    entry_date = models.DateTimeField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    @property
    def total_price(self):
        price = self.room * 120
        return price
