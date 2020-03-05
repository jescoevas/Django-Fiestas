from django.contrib import admin
from .models import Building

# Register your models here.

class BuildingAdmin(admin.ModelAdmin):
    list_display = ('address', 'capacity', 'decision', 'owner',)
    list_filter = ('capacity', 'decision')

admin.site.register(Building, BuildingAdmin)