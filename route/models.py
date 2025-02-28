from django.db import models

"""
rota, mekan vs
"""


class Place(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    created_by = models.ForeignKey('account.UserBase', on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

class TestModel(models.Model):
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=100)
