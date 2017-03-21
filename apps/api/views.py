from django.http import JsonResponse
from rest_framework.decorators import api_view

from .models import NRCS_Locations
from .serializers import NRCS_LocationsSerializer

@api_view(['GET'])
def get_snowpack_data(request):
    locations = NRCS_Locations.objects.all()
    serializer = NRCS_LocationsSerializer(locations, many=True)
    return JsonResponse(serializer.data, safe=False)
