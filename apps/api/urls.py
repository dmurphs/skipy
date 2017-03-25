from django.conf.urls import url
from .views import LocationList, LocationData

urlpatterns = [
    url(r'^locations/', LocationList.as_view(), name='location-list'),
    url(r'^(?P<station_id>\w{0,7})/(?P<year>\w{4})/$', LocationData.as_view(), name='location-data'),
]
