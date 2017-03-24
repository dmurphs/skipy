from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import include, url
from django.contrib import admin

from apps.api import urls as api_urls

base_patterns = [
    url(r'^api/', include(api_urls)),
    url(r'^admin/', admin.site.urls),
]

debug_patterns = static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns = base_patterns + debug_patterns
else:
    urlpatterns = base_patterns
