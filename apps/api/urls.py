from django.conf.urls import url
from .views import get_snowpack_data

urlpatterns = [
    url(r'^$', get_snowpack_data),
]
