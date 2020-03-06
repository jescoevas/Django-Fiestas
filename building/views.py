from django.shortcuts import render
from building.models import Building

def buildings(request):
    template = 'buildings.html'
    buildings = Building.objects.all()
    context = {'buildings':buildings}
    return render(request, template, context)
