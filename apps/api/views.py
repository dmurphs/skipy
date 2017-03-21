from django.http import JsonResponse
from rest_framework.decorators import api_view

from .models import NRCS_Locations, NRCS_MonthlySnow
from .serializers import NRCS_LocationsSerializer, NRCS_MonthlySnowSerializer

@api_view(['GET'])
def get_locations(request):
    '''Get all data collection sites
       query: /api/locations'''
    locations = NRCS_Locations.objects.all()
    serializer = NRCS_LocationsSerializer(locations, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def get_all_location_data(request, station_id):
    '''Get all monthly snow data for location
       example query: /api/get/12D10'''
    location = NRCS_Locations.objects.get(pk=station_id)
    all_snow_data = NRCS_MonthlySnow.objects.filter(location=location)
    serializer = NRCS_MonthlySnowSerializer(all_snow_data, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def get_location_data_for_year(request, station_id, year):
    '''Get data from specific year for location
       example query: /api/get/12D10/1999)'''
    location = NRCS_Locations.objects.get(pk=station_id)
    year_snow_data = NRCS_MonthlySnow.objects.filter(location=location,water_year=year)
    serializer = NRCS_MonthlySnowSerializer(year_snow_data, many=True)
    return JsonResponse(serializer.data, safe=False)
