from django.db import models
from geolocation_fields.models import fields
from django_countries.fields import CountryField

"""
rota, mekan vs
"""


class Place(models.Model):
    name = models.CharField(max_length=255)
    country = CountryField(default='TR')
    description = models.TextField()
    geolocation = fields.PointField(verbose_name='Marker')
    created_by = models.ForeignKey('account.UserBase', on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

class TestModel(models.Model):
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=100)
