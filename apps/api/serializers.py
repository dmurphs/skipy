from rest_framework import serializers

from .models import NRCS_Locations, NRCS_MonthlySnow

class NRCS_LocationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NRCS_Locations
        fields = ('site_name', 'elev', 'lat', 'lon', 'state', 'county')

class NRCS_MonthlySnowSerializer(serializers.ModelSerializer):
    class Meta:
        model = NRCS_MonthlySnow
        fields = ('collection_date', 'snow_depth', 'snow_water_equivalent')
