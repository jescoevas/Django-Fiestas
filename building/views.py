from django.shortcuts import render
from .models import get_accepted_buildings_by_address, get_building_by_id
from roles.models import setUser

def search_buildings(request):
    template = 'search_buildings.html'
    context = {}
    setUser(request, context)

    if request.method == 'GET':
        return render(request,template,context)
    
    search = request.POST.get('search')
    buildings = get_accepted_buildings_by_address(search)
    context['buildings'] = buildings
    return render(request, template, context)

def show_building(request, id):
    template = 'show_building.html'
    building = get_building_by_id(id)
    context = {'building':building}
    setUser(request, context)
    return render(request, template, context)