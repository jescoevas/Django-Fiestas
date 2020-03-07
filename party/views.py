from django.shortcuts import render
from .models import Party, Request


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