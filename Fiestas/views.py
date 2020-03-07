from django.shortcuts import render
from building.models import Building
from party.models import Party, Request
from roles.models import Owner, Customer, Administrator

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
    if 'id' in request.COOKIES.keys():
        context['userId'] = request.COOKIES['id']
        if 'isOwner' in request.COOKIES.keys():
            context['isOwner'] = True
        elif 'isCustomer' in request.COOKIES.keys():
            context['isCustomer'] = True
        else:
            context['isAdmin'] = True
    
    return render(request, template, context)
