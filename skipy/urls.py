from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import include, url
from django.contrib import admin

from apps.api import urls as api_urls
from apps.home import views as home_views
from apps.maps import urls as maps_urls

base_patterns = [
    url(r'^$', home_views.index, name='home'),
    url(r'^api/', include(api_urls)),
    url(r'^maps/', include(maps_urls)),
    url(r'^admin/', admin.site.urls),
]

debug_patterns = static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns = base_patterns + debug_patterns
else:
    urlpatterns = base_patterns