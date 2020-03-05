from django.db import models

# Create your models here.

class Administrator(models.Model):
    name = models.CharField(max_length=20, blank=False)
    surname = models.CharField(max_length=20, blank=False)
    email = models.EmailField(blank=False)
    phone = models.CharField(max_length=14)


class Owner(models.Model):
    name = models.CharField(max_length=20, blank=False)
    surname = models.CharField(max_length=20, blank=False)
    email = models.EmailField(blank=False)
    phone = models.CharField(max_length=14)

class Customer(models.Model):
    name = models.CharField(max_length=20, blank=False)
    surname = models.CharField(max_length=20, blank=False)
    email = models.EmailField(blank=False)
    phone = models.CharField(max_length=14)