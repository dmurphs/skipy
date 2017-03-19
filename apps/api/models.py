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

class NRCS_MonthlySnow(models.Model):
    location = models.ForeignKey(NRCS_Locations)
    Water_Year = models.PositiveSmallIntegerField()
    Jan_collection_date = models.DateField(null=True)
    Jan_snow_depth = models.PositiveSmallIntegerField(null=True)
    Jan_snow_water_equivalent = models.DecimalField(null=True,max_digits=5,decimal_places=2)
    Feb_collection_date = models.DateField(null=True)
    Feb_snow_depth = models.PositiveSmallIntegerField(null=True)
    Feb_snow_water_equivalent = models.DecimalField(null=True,max_digits=5,decimal_places=2)
    Mar_collection_date = models.DateField(null=True)
    Mar_snow_depth = models.PositiveSmallIntegerField(null=True)
    Mar_snow_water_equivalent = models.DecimalField(null=True,max_digits=5,decimal_places=2)
    Apr_collection_date = models.DateField(null=True)
    Apr_snow_depth = models.PositiveSmallIntegerField(null=True)
    Apr_snow_water_equivalent = models.DecimalField(null=True,max_digits=5,decimal_places=2)
    May_collection_date = models.DateField(null=True)
    May_snow_depth = models.PositiveSmallIntegerField(null=True)
    May_snow_water_equivalent = models.DecimalField(null=True,max_digits=5,decimal_places=2)
    Jun_collection_date = models.DateField(null=True)
    Jun_snow_depth = models.PositiveSmallIntegerField(null=True)
    Jun_snow_water_equivalent = models.DecimalField(null=True,max_digits=5,decimal_places=2)
    Jul_collection_date = models.DateField(null=True)
    Jul_snow_depth = models.PositiveSmallIntegerField(null=True)
    Jul_snow_water_equivalent = models.PositiveSmallIntegerField(null=True)
    Aug_collection_date = models.DateField(null=True)
    Aug_snow_depth = models.PositiveSmallIntegerField(null=True)
    Aug_snow_water_equivalent = models.DecimalField(null=True,max_digits=5,decimal_places=2)
    Sep_collection_date = models.DateField(null=True)
    Sep_snow_depth = models.PositiveSmallIntegerField(null=True)
    Sep_snow_water_equivalent = models.DecimalField(null=True,max_digits=5,decimal_places=2)
    Oct_collection_date = models.DateField(null=True)
    Oct_snow_depth = models.PositiveSmallIntegerField(null=True)
    Oct_snow_water_equivalent = models.DecimalField(null=True,max_digits=5,decimal_places=2)
    Nov_collection_date = models.DateField(null=True)
    Nov_snow_depth = models.PositiveSmallIntegerField(null=True)
    Nov_snow_water_equivalent = models.DecimalField(null=True,max_digits=5,decimal_places=2)
    Dec_collection_date = models.DateField(null=True)
    Dec_snow_depth = models.PositiveSmallIntegerField(null=True)
    Dec_snow_water_equivalent = models.DecimalField(null=True,max_digits=5,decimal_places=2)