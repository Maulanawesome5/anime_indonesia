from django.contrib import admin
from .models import Anime, Studio


# Register your models here.
class ContentsAdmin(admin.ModelAdmin):
    readonly_fields = ["slug", "updated", "created"]

admin.site.register(Anime, admin_class=ContentsAdmin)
admin.site.register(Studio, admin_class=ContentsAdmin)
