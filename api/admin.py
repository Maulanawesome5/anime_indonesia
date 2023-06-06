from django.contrib import admin
from .models import Anime, Studio


# Register your models here.
class AnimeAdmin(admin.ModelAdmin):
    readonly_fields = ["slug", "updated", "created"]

class StudioAdmin(admin.ModelAdmin):
    readonly_fields = ["slug", "updated", "created"]

admin.site.register(Anime, admin_class=AnimeAdmin)
admin.site.register(Studio, admin_class=StudioAdmin)
