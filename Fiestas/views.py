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
    try:
        userId = request.COOKIES['id']
        context['userId'] = userId
        try:
            owner = Owner.objects.get(id = userId)
            print(owner)
            context['isOwner'] = True
        except Exception:
            try:
                customer = Customer.objects.get(id = userId)
                print(customer)
                context['isCustomer'] = True
            except Exception:
                try:
                    admin = Administrator.objects.get(id = userId)
                    print(admin)
                    context['isAdmin'] = True
                except Exception:
                    print(Exception)
    except Exception:
        print(Exception)
    return render(request, template, context)
