from __future__ import unicode_literals

from django.db import models

class NRCS_Locations(models.Model):
    site_name = models.CharField(max_length=100)
    station = models.CharField(max_length=7,primary_key=True)
    ntwk = models.CharField(max_length=5)
    elev = models.IntegerField()
    lat = models.DecimalField(max_digits=6, decimal_places=2)
    lon = models.DecimalField(max_digits=6, decimal_places=2)
    installed = models.PositiveSmallIntegerField()
    state = models.CharField(max_length=2)
    county = models.CharField(max_length=100)
    hydrologic_unit = models.CharField(max_length=255)
    shef = models.CharField(max_length=7)

class NRCS_MonthlySnow(models.Model):
    location = models.ForeignKey(NRCS_Locations)
    water_year = models.PositiveSmallIntegerField()
    collection_month = models.PositiveSmallIntegerField()
    collection_date = models.DateField(null=True)
    snow_depth = models.PositiveSmallIntegerField(null=True)
    snow_water_equivalent = models.DecimalField(null=True,max_digits=5,decimal_places=2)