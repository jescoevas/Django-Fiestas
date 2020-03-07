from django.contrib import admin
from .models import Party, Request

# Register your models here.

class RequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'message', 'decision',)
    list_filter = ('decision',)

class PartyAdmin(admin.ModelAdmin):
    list_display = ('id', 'price', 'startDate', 'endDate', 'numberOfAttendees',)
    list_filter = ('price', 'startDate', 'endDate', 'numberOfAttendees',)

admin.site.register(Request, RequestAdmin)
admin.site.register(Party, PartyAdmin)