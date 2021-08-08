import os
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('apps.Client.urls')),
    path("", include('apps.Division.urls')),
    path("", include('apps.Drawing.urls')),
    path("", include('apps.Part.urls'))
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
