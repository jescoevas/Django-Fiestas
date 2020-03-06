from django.db import models
from building.models import Building
from roles.models import Customer

# Create your models here.

decisions = (('PENDING','P'),('ACCEPTED','A'),('REJECTED','R'))

class Request(models.Model):
    message = models.CharField(max_length=100, blank=False)
    decision = models.CharField(max_length=10,default='PENDING', choices=decisions)
    building = models.ForeignKey(Building, null=False, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.building.address} - {self.customer.name} ({self.decision})'

class Party(models.Model):
    name = models.CharField(max_length=20, default='')
    description = models.CharField(max_length=256,blank=False)
    price = models.PositiveIntegerField(null=False)
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()
    numberOfAttendees = models.PositiveIntegerField(null=False)
    description = models.CharField(max_length=256,blank=False)
    picture = models.URLField(default='')
    request = models.ForeignKey(Request, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.request.building.address} - {self.price} - ({self.startDate} - {self.endDate})'