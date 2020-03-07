from django.db import models
from roles.models import Owner, get_owner_by_id

# Create your models here.

decisions = (('PENDING','P'),('ACCEPTED','A'),('REJECTED','R'))

class Building(models.Model):
    address = models.CharField(max_length=20, blank=False)
    capacity = models.PositiveIntegerField(null=False)
    conditions = models.CharField(max_length=256,blank=False)
    picture = models.URLField(default='')
    decision = models.CharField(max_length=10,default='PENDING', choices=decisions)
    owner = models.ForeignKey(Owner, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.address} - {self.capacity}'

def get_accepted_buildings():
    return Building.objects.filter(decision='ACCEPTED')

def get_pending_buildings():
    return Building.objects.filter(decision = 'PENDING')

def get_rejected_buildings():
    return Building.objects.filter(decision = 'REJECTED')

def get_all_buildings():
    return Building.objects.all()

def get_accepted_buildings_by_address(address):
    return Building.objects.filter(address__icontains = address ).filter(decision = 'ACCEPTED')

def get_building_by_id(id):
    return Building.objects.get(id=id)

def get_buildings_by_owner_id(id):
    owner = get_owner_by_id(id)
    return Building.objects.filter(owner = owner)