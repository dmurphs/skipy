from rest_framework import generics

from django.http import JsonResponse
from rest_framework.decorators import api_view

from .models import NRCS_Locations, NRCS_MonthlySnow
from .serializers import NRCS_LocationsSerializer, NRCS_MonthlySnowSerializer

class LocationList(generics.ListAPIView):
    '''Get all locations'''
    queryset = NRCS_Locations.objects.all()
    serializer_class = NRCS_LocationsSerializer

class LocationData(generics.ListAPIView):
    '''Get all monthly snow data for location
       example query: /api/12D10/1999'''

    def get_queryset(self):
        station_id = self.kwargs['station_id']
        year = self.kwargs['year']
        location = NRCS_Locations.objects.get(pk=station_id)
        return NRCS_MonthlySnow.objects.filter(location=location,water_year=year)

    serializer_class = NRCS_MonthlySnowSerializer
