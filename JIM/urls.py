from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('apps.Client.urls')),
    path("", include('apps.Division.urls')),
    path("", include('apps.Drawing.urls')),
    path("", include('apps.Part.urls'))
]
