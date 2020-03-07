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


def set_user(request, context):
    if is_authenticated(request):
        context['userId'] = request.COOKIES['id']
        if is_owner(request):
            context['isOwner'] = True
        elif is_customer(request):
            context['isCustomer'] = True
        else:
            context['isAdmin'] = True
    
def is_authenticated(request):
    if 'id' in request.COOKIES.keys():
        return True
    else:
        return False

def get_user(request):
    if is_authenticated(request):
        id = request.COOKIES['id']
        if is_owner(request):
            return get_owner_by_id(id)
        elif is_customer(request):
            return get_customer_by_id(id)
        else:
            return get_admin_by_id(id)
    else:
        return None

def is_owner(request):
    if 'isOwner' in request.COOKIES.keys():
        return True
    else:
        return False

def get_owner_by_id(id):
    return Owner.objects.get(id=id)

def is_customer(request):
    if 'isCustomer' in request.COOKIES.keys():
        return True
    else:
        return False

def get_customer_by_id(id):
    return Customer.objects.get(id=id)

def is_admin(request):
    if 'isAdmin' in request.COOKIES.keys():
        return True
    else:
        return False

def get_admin_by_id(id):
    return Administrator.objects.get(id=id)