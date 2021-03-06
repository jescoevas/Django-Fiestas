from django.shortcuts import render, redirect
from .models import Building, get_accepted_buildings_by_address, get_building_by_id, get_buildings_by_owner_id, get_pending_buildings
from roles.models import set_user, get_user, is_admin, is_owner
from django.contrib import messages

def search_buildings(request):
    template = 'search_buildings.html'
    context = {}
    set_user(request, context)

    if request.method == 'GET':
        return render(request,template,context)
    
    search = request.POST.get('search')
    buildings = get_accepted_buildings_by_address(search)
    context['buildings'] = buildings
    return render(request, template, context)

def show_building(request, id):
    building = get_building_by_id(id)
    user = get_user(request)
    if building.decision == 'ACCEPTED' or building.owner == user or is_admin(request):
        template = 'show_building.html'
        context = {'building':building}
        set_user(request, context)
        if is_admin(request) and building.decision == 'PENDING':
            context['choose'] = True
        return render(request, template, context)
    else:
        return redirect('index')

def owner_buildings(request, userId):
    if is_owner(request):
        template = 'owner_buildings.html'
        buildings = get_buildings_by_owner_id(userId)
        context = {'buildings':buildings}
        set_user(request, context)
        return render(request, template, context)
    else:
        return redirect('index')

def new_building(request):
    if is_owner(request):
        template = 'new_building.html'
        context = {}
        set_user(request, context)
        if request.method == 'GET':
            return render(request, template, context)
        
        address = request.POST.get('address')
        capacity = request.POST.get('capacity')
        conditions = request.POST.get('conditions')
        picture = request.POST.get('picture')
        owner = get_user(request)

        building = Building(address = address, capacity = capacity, conditions = conditions, 
                            picture = picture, owner = owner)
        building.save()
        return redirect(f'/building/owner/{owner.id}/buildings')

    else:
        return redirect('index')

def admin_buildings(request):
    if is_admin(request):
        template = 'admin_buildings.html'
        buildings = get_pending_buildings()
        context = {'buildings':buildings}
        set_user(request, context)
        return render(request, template, context)
    else:
        return redirect('index')

def admin_choice(request, id, choice):
    if is_admin(request):
        building = get_building_by_id(id)
        if choice == 'accept':
            building.decision = 'ACCEPTED'
        else:
            building.decision = 'REJECTED'
        building.save()
        return redirect('index')
    else:
        return redirect('index')