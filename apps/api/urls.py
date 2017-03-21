from django.conf.urls import url
from .views import get_locations, get_all_location_data, get_location_data_for_year

urlpatterns = [
    url(r'^locations/', get_locations),
    url(r'^(?P<station_id>\w{0,7})/$', get_all_location_data),
    url(r'^(?P<station_id>\w{0,7})/(?P<year>\w{4})/$', get_location_data_for_year)
]
