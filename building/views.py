from django.shortcuts import render
from .models import Building, get_accepted_buildings_by_address
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