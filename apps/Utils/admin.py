from django.contrib import admin

from apps.Client.models import Client
from apps.Division.models import Division
from apps.Drawing.models import Drawing
from apps.Part.models import Part, Material, OutSource

admin.site.register(Client)
admin.site.register(Division)
admin.site.register(Drawing)
admin.site.register(Part)
admin.site.register(Material)
admin.site.register(OutSource)
