from django.shortcuts import render
from building.models import Building

def index(request):
    template = 'index.html'
    buildings = Building.objects.all()
    context = {'buildings':buildings}
    return render(request, template, context)