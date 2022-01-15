from django.contrib import admin

from apps.client.models import Client
from apps.division.models import Division
from apps.drawing.models import Drawing
from apps.part.models import Part, Material, OutSource, File

admin.site.register(Client)
admin.site.register(Division)
admin.site.register(Drawing)
admin.site.register(File)
admin.site.register(Part)
admin.site.register(Material)
admin.site.register(OutSource)
