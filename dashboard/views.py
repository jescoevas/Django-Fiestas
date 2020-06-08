from django.shortcuts import render, redirect
from roles.models import set_user, is_admin
from .models import get_percentage_buildings, get_percentage_party_requests, get_percentage_attend_requests

# Create your views here.

def show(request):
    if is_admin(request):
        template = 'dashboard.html'
        context = {}
        set_user(request, context)
        
        accepted_buildings = get_percentage_buildings('ACCEPTED')
        context['accepted_buildings'] = accepted_buildings
        rejected_buildings = get_percentage_buildings('REJECTED')
        context['rejected_buildings'] = rejected_buildings
        pending_buildings = get_percentage_buildings('PENDING')
        context['pending_buildings'] = pending_buildings

        accepted_parties = get_percentage_party_requests('ACCEPTED')
        context['accepted_parties'] = accepted_parties
        rejected_parties = get_percentage_party_requests('REJECTED')
        context['rejected_parties'] = rejected_parties
        pending_parties = get_percentage_party_requests('PENDING')
        context['pending_parties'] = pending_parties

        accepted_attend_requests = get_percentage_attend_requests('ACCEPTED')
        context['accepted_attend_requests'] = accepted_attend_requests
        rejected_attend_requests = get_percentage_attend_requests('REJECTED')
        context['rejected_attend_requests'] = rejected_attend_requests
        pending_attend_requests = get_percentage_attend_requests('PENDING')
        context['pending_attend_requests'] = pending_attend_requests

        return render(request, template, context)
    else:
        return redirect('index')