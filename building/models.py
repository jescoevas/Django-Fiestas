from django.db import models
from roles.models import Owner

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

def get_all_buildings():
    return Building.objects.all()

def get_accepted_buildings_by_address(address):
    return Building.objects.filter(address__icontains = address ).filter(decision = 'ACCEPTED')