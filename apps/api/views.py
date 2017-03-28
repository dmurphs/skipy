from rest_framework import generics

from django.http import JsonResponse
from rest_framework.decorators import api_view

from .models import NRCS_Locations, NRCS_MonthlySnow
from .serializers import NRCS_LocationsSerializer, NRCS_MonthlySnowSerializer

class LocationList(generics.ListAPIView):
    '''Get all locations'''
    queryset = NRCS_Locations.objects.all()
    serializer_class = NRCS_LocationsSerializer

class MonthlySnowList(generics.ListAPIView):
    '''Get all locations'''
    serializer_class = NRCS_MonthlySnowSerializer

    def get_queryset(self):
        year = int(self.kwargs['year'])
        month = int(self.kwargs['month'])

        return NRCS_MonthlySnow.objects.filter(collection_date__year=year,
                                               collection_date__month=month)
