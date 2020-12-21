from django.contrib import admin
from .models import dialecticapp

class DialecticAdmin(admin.ModelAdmin):
    list_display=['date', 'updated', 'night', 'morning', 'daytime', 'evening', 'beforeSleep', 'notes']
    list_display_links=['night', 'morning', 'daytime', 'evening', 'beforeSleep', 'notes']

admin.site.register(dialecticapp, DialecticAdmin)

