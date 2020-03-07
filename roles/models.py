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


def isAuthenticated(request):
    if 'id' in request.COOKIES.keys():
        return True
    else:
        return False

def isOwner(request):
    if 'isOwner' in request.COOKIES.keys():
        return True
    else:
        return False

def isCustomer(request):
    if 'isCustomer' in request.COOKIES.keys():
        return True
    else:
        return False

def isAdmin(request):
    if 'isAdmin' in request.COOKIES.keys():
        return True
    else:
        return False

def setUser(request, context):
    if isAuthenticated(request):
        context['userId'] = request.COOKIES['id']
        if isOwner(request):
            context['isOwner'] = True
        elif isCustomer(request):
            context['isCustomer'] = True
        else:
            context['isAdmin'] = True
    
