from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Owner, Customer

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
        print('Dentro de owner')
        try:
            owner = Owner(name=name, surname=surname, email=email, phone=phone, password=password)
            owner.save()
            return redirect('/login')
        except:
            messages.error(request,'Sign up failed')
            return render(request,template)
    else:
        print('Dentro de customer')
        try:
            customer = Customer(name=name, surname=surname, email=email, phone=phone, password=password)
            customer.save()
            return redirect('/login')
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
    return response