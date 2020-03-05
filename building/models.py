from django.db import models
from roles.models import Owner

# Create your models here.

decisions = (('P','PENDING'),('A','ACCEPTED'),('R','REJECTED'))

class Building(models.Model):
    address = models.CharField(max_length=20, blank=False)
    capacity = models.PositiveIntegerField(null=False)
    conditions = models.CharField(max_length=256,blank=False)
    decision = models.CharField(max_length=10,default='PENDING', choices=decisions)
    owner = models.ForeignKey(Owner, null=False, on_delete=models.CASCADE)