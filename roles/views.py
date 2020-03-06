from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Owner

# Create your views here.

def signup(request):
    if request.method == 'GET':
        template='signup.html'
        return render(request, template)
    
    name = request.POST.get('name')
    surname = request.POST.get('surname')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    password = request.POST.get('password')

    try:
        owner = Owner(name=name, surname=surname, email=email, phone=phone, password=password)
        owner.save()
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
    
    try:
        owner = Owner.objects.get(email=email)
        return render(request,template)
    except:
        messages.error(request,'Owner does not exist')
        return render(request,template)