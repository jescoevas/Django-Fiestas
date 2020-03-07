from django.shortcuts import render
from building.models import get_accepted_buildings
from party.models import get_accepted_parties
from roles.models import setUser

def index(request):
    template = 'index.html'
    buildings = get_accepted_buildings()
    parties = get_accepted_parties()
    context = {'buildings':buildings, 'parties':parties, 'nav':'index'}
    setUser(request, context)
    return render(request, template, context)
