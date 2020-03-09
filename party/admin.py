from django.contrib import admin
from .models import Party, Request, AttendRequest

# Register your models here.

class RequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'message', 'decision',)
    list_filter = ('decision',)

class PartyAdmin(admin.ModelAdmin):
    list_display = ('id', 'price', 'startDate', 'endDate', 'numberOfAttendees',)
    list_filter = ('price', 'startDate', 'endDate', 'numberOfAttendees',)

class AttendRequestAdmin(admin.ModelAdmin):
    list_display = ('customer', 'party', 'decision',)
    list_filter = ('customer', 'party', 'decision',)

admin.site.register(Request, RequestAdmin)
admin.site.register(Party, PartyAdmin)
admin.site.register(AttendRequest, AttendRequestAdmin)