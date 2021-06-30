import json
from django.contrib import admin


""": hybrid, roadmap, satellite, terrain"""
from route.models import Place


class PlaceAdmin(admin.ModelAdmin):
    pass

admin.site.register(Place, PlaceAdmin)
