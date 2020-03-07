from django.shortcuts import render
from .models import get_accepted_parties_by_name, get_party_by_id
from roles.models import setUser


def search_parties(request):
    template = 'search_parties.html'
    context = {}
    setUser(request, context)

    if request.method == 'GET':
        return render(request,template,context)
    
    search = request.POST.get('search')
    parties = get_accepted_parties_by_name(search)
    context['parties'] = parties
    return render(request, template, context)

def show_party(request, id):
    template = 'show_party.html'
    party = get_party_by_id(id)
    context = {'party':party}
    setUser(request, context)
    return render(request, template, context)

