from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

API_ROOT = 'api/v2/'

urlpatterns = [
    path(API_ROOT + 'admin/', admin.site.urls),
    path(API_ROOT, include('apps.Client.urls')),
    path(API_ROOT, include('apps.Division.urls')),
    path(API_ROOT, include('apps.Drawing.urls')),
    path(API_ROOT, include('apps.Part.urls')),
    path(API_ROOT, include('apps.Auth.urls'))
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
