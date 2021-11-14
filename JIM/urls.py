from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

API_ROOT = 'api/v2/'

urlpatterns = [
    path(API_ROOT + 'admin/', admin.site.urls),
    path(API_ROOT, include('apps.authentication.urls')),
    path(API_ROOT, include('apps.client.urls')),
    path(API_ROOT, include('apps.division.urls')),
    path(API_ROOT, include('apps.drawing.urls')),
    path(API_ROOT, include('apps.part.urls'))
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
