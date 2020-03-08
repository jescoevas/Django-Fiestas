from django.shortcuts import render, redirect
from .models import Party, Request, get_accepted_parties_by_name, get_party_by_id, get_parties_by_customer_id
from roles.models import set_user, is_customer, get_user
from building.models import get_building_by_id


def search_parties(request):
    template = 'search_parties.html'
    context = {}
    set_user(request, context)

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
    set_user(request, context)
    return render(request, template, context)
    
def customer_parties(request, id):
    if is_customer(request):
        template = 'customer_parties.html'
        parties = get_parties_by_customer_id(id)
        context = {'parties':parties}
        set_user(request, context)
        return render(request, template, context)
    else:
        return redirect('index')

def new_party(request, id):
    if is_customer(request):
        template = 'new_party.html'
        building = get_building_by_id(id)
        context = {'building':building}
        set_user(request, context)
        if request.method == 'GET':
            return render(request, template, context)
        

        message = request.POST.get('message')
        name = request.POST.get('name')
        description = request.POST.get('description')
        attendees = request.POST.get('attendees')
        startdate = request.POST.get('startdate')
        enddate = request.POST.get('enddate')
        picture = request.POST.get('picture')
        price = request.POST.get('price')
        customer = get_user(request)

        request = Request(message = message, building = building, customer = customer)
        request.save()

        party = Party(name = name, price=price, description = description, numberOfAttendees = attendees, 
                        startDate = startdate, endDate = enddate, picture = picture, request = request)
        party.save()

        return redirect(f'/party/customer/{customer.id}/parties')

    else:
        return redirect('index')