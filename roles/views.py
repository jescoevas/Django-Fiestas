from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Owner, Customer, Administrator

# Create your views here.

def signup(request):
    template = 'signup.html'
    if request.method == 'GET':
        return render(request, template)
    
    name = request.POST.get('name')
    surname = request.POST.get('surname')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    role = request.POST.get('role')
    password = request.POST.get('password')

    if role == 'owner':
        try:
            owner = Owner(name=name, surname=surname, email=email, phone=phone, password=password)
            owner.save()
            return redirect('/roles/login')
        except:
            messages.error(request,'Sign up failed')
            return render(request,template)
    else:
        try:
            customer = Customer(name=name, surname=surname, email=email, phone=phone, password=password)
            customer.save()
            return redirect('/roles/login')
        except:
            messages.error(request,'Sign up failed')
            return render(request,template)

    
    

def login(request):
    template='login.html'
    if request.method == 'GET':
        return render(request,template)
    
    email = request.POST.get('email')
    password = request.POST.get('password')
    context = {'email_exists':email}

    try:
        owner = Owner.objects.get(email=email)
        if owner.password == password:
            response = redirect('/index')
            response.set_cookie('id', owner.id)
            response.set_cookie('isOwner',True)
            return response
        else:
            context['password_is_not_correct'] = 'Password is not correct'
            return render(request,template,context)
    except:
        try:
            customer = Customer.objects.get(email=email)
            if customer.password == password:
                response = redirect('/index')
                response.set_cookie('id', customer.id)
                response.set_cookie('isCustomer',True)
                return response
            else:
                context['password_is_not_correct'] = 'Password is not correct'
                return render(request,template,context)
        except:
            try:
                admin = Administrator.objects.get(email=email)
                if admin.password == password:
                    response = redirect('/index')
                    response.set_cookie('id', admin.id)
                    response.set_cookie('isAdmin',True)
                    return response
                else:
                    context['password_is_not_correct'] = 'Password is not correct'
                    return render(request,template,context)
            except:
                context['user_does_not_exist'] = 'User does not exist'
                return render(request,template,context)

def logout(request):
    response = redirect('/index')
    response.delete_cookie('id')
    if 'isOwner' in request.COOKIES.keys():
        response.delete_cookie('isOwner')
    elif 'isCustomer' in request.COOKIES.keys():
        response.delete_cookie('isCustomer')
    else:
        response.delete_cookie('isAdmin')
    return response

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
    

        