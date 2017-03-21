from rest_framework import serializers

from models import NRCS_Locations

class NRCS_LocationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NRCS_Locations
        fields = ('site_name', 'elev', 'lat', 'lon', 'state', 'county')
        