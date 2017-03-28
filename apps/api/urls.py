from django.conf.urls import url
from .views import MonthlySnowList, LocationList

urlpatterns = [
    url(r'^locations/', LocationList.as_view(), name='locations'),
    url(r'^monthlySnowData/(?P<year>\w{4})/(?P<month>\w{2})/$', MonthlySnowList.as_view(), name='location-data'),
]
