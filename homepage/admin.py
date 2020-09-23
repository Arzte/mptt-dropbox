from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from homepage.models import File


admin.site.register(File, DraggableMPTTAdmin)
