from django.shortcuts import render
from building.models import Building
from party.models import Party, Request

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
    try:
        context['userId'] = request.COOKIES['id']
    except Exception:
        print(Exception)
    return render(request, template, context)

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

def search_parties(request):
    template = 'search_parties.html'
    context = {}
    try:
        context['userId'] = request.COOKIES['id']
    except Exception:
        print(Exception)

    if request.method == 'GET':
        return render(request,template,context)
    
    search = request.POST.get('search')
    requests = Request.objects.filter(decision='ACCEPTED')
    all_parties = Party.objects.filter(name__icontains = search)
    parties = []
    for p in all_parties:
        if p.request in requests:
            parties.append(p)
    context['parties'] = parties
    return render(request, template, context)