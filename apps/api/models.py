from __future__ import unicode_literals

from django.db import models

class NRCS_Locations(models.Model):
    Site_Name = models.CharField(max_length=100)
    Station = models.CharField(max_length=7,primary_key=True)
    Ntwk = models.CharField(max_length=5)
    Elev = models.IntegerField()
    Lat = models.DecimalField(max_digits=6, decimal_places=2)
    Lon = models.DecimalField(max_digits=6, decimal_places=2)
    installed = models.PositiveSmallIntegerField()
    state = models.CharField(max_length=2)
    County = models.CharField(max_length=100)
    Hydrologic_Unit = models.CharField(max_length=255)
    SHEF = models.CharField(max_length=7)