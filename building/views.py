from django.shortcuts import render
from .models import Building

def search_buildings(request):
    template = 'search_buildings.html'
    context = {}
    try:
        context['userId'] = request.COOKIES['id']
    except Exception:
        print(Exception)

    if request.method == 'GET':
        return render(request,template,context)
    
    search = request.POST.get('search')
    buildings = Building.objects.filter(address__icontains = search ).filter(decision = 'ACCEPTED')
    context['buildings'] = buildings
    return render(request, template, context)