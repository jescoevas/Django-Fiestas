from django.shortcuts import render
from building.models import Building
from party.models import Party, Request
from roles.models import Owner, Customer, Administrator
from roles.views import setUser

def index(request):
    template = 'index.html'
    buildings = Building.objects.filter(decision='ACCEPTED')
    requests = Request.objects.filter(decision='ACCEPTED')
    all_parties = Party.objects.all()
    parties = []
    for p in all_parties:
        if p.request in requests:
            parties.append(p)
    context = {'buildings':buildings, 'parties':parties, 'nav':'index'}
    setUser(request, context)
    
    return render(request, template, context)
