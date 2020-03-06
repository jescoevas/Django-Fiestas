from django.shortcuts import render
from building.models import Building
from party.models import Party

def index(request):
    template = 'index.html'
    buildings = Building.objects.all()
    parties = Party.objects.all()
    context = {'buildings':buildings, 'parties':parties, 'nav':'index'}
    return render(request, template, context)
