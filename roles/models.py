from django.db import models

# Create your models here.

class Administrator(models.Model):
    name = models.CharField(max_length=20, blank=False)
    surname = models.CharField(max_length=20, blank=False)
    email = models.EmailField(blank=False)
    password = models.CharField(max_length=20, default='')
    phone = models.CharField(max_length=14)

    def __str__(self):
        return self.name


class Owner(models.Model):
    name = models.CharField(max_length=20, blank=False)
    surname = models.CharField(max_length=20, blank=False)
    email = models.EmailField(blank=False)
    password = models.CharField(max_length=20, default='')
    phone = models.CharField(max_length=14)

    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length=20, blank=False)
    surname = models.CharField(max_length=20, blank=False)
    email = models.EmailField(blank=False)
    password = models.CharField(max_length=20, default='')
    phone = models.CharField(max_length=14)

    def __str__(self):
        return self.name