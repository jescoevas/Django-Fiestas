from django.db import models
from building.models import Building
from roles.models import Customer

# Create your models here.

decisions = (('P','PENDING'),('A','ACCEPTED'),('R','REJECTED'))

class Request(models.Model):
    message = models.CharField(max_length=100, blank=False)
    decision = models.CharField(max_length=10,default='PENDING', choices=decisions)
    building = models.ForeignKey(Building, null=False, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, null=False, on_delete=models.CASCADE)

class Party(models.Model):
    description = models.CharField(max_length=256,blank=False)
    price = models.PositiveIntegerField(null=False)
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()
    numberOfAttendees = models.PositiveIntegerField(null=False)
    description = models.CharField(max_length=256,blank=False)
    request = models.ForeignKey(Request, null=False, on_delete=models.CASCADE)