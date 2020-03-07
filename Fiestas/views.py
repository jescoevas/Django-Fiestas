from django.shortcuts import render
from building.models import get_accepted_buildings
from party.models import get_accepted_parties
from roles.models import set_user

def index(request):
    template = 'index.html'
    buildings = get_accepted_buildings()
    parties = get_accepted_parties()
    context = {'buildings':buildings, 'parties':parties, 'nav':'index'}
    set_user(request, context)
    return render(request, template, context)
