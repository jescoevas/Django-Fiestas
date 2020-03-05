from django.contrib import admin
from .models import Administrator, Owner, Customer

# Register your models here.

class AdministratorAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'email','phone',)


class OwnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'email','phone',)


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'email','phone',)

admin.site.register(Administrator, AdministratorAdmin)
admin.site.register(Owner, OwnerAdmin)
admin.site.register(Customer, CustomerAdmin)