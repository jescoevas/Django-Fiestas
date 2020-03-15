from django.db import models
from building.models import Building, get_buildings_by_owner_id
from roles.models import Customer, get_customer_by_id, get_owner_by_id

# Create your models here.

decisions = (('PENDING','P'),('ACCEPTED','A'),('REJECTED','R'))

class Request(models.Model):
    message = models.CharField(max_length=100, blank=False)
    decision = models.CharField(max_length=10,default='PENDING', choices=decisions)
    building = models.ForeignKey(Building, null=False, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.building.address} - {self.customer.name} ({self.decision})'

class Party(models.Model):
    name = models.CharField(max_length=20, default='')
    description = models.CharField(max_length=256,blank=False)
    price = models.PositiveIntegerField(null=False)
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()
    numberOfAttendees = models.PositiveIntegerField(null=False)
    description = models.CharField(max_length=256,blank=False)
    picture = models.URLField(default='')
    request = models.ForeignKey(Request, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.request.building.address}'

class AttendRequest(models.Model):
    decision = models.CharField(max_length=10,default='PENDING', choices=decisions)
    customer = models.ForeignKey(Customer, null=False, on_delete=models.CASCADE)
    party = models.ForeignKey(Party, null=False, on_delete=models.CASCADE)

def get_accepted_parties():
    requests = Request.objects.filter(decision='ACCEPTED')
    all_parties = Party.objects.all()
    res = []
    for p in all_parties:
        if p.request in requests:
            res.append(p)
    return res

def get_pending_requests_by_owner_id(id):
    buildings = get_buildings_by_owner_id(id)
    pending_requests = Request.objects.filter(decision = 'PENDING')
    res = []
    for r in pending_requests:
        if r.building in buildings:
            res.append(r)
    return res

def get_accepted_parties_by_name(name):
    requests = Request.objects.filter(decision='ACCEPTED')
    all_parties = Party.objects.filter(name__icontains = name)
    res = []
    for p in all_parties:
        if p.request in requests:
            res.append(p)
    return res

def get_party_by_id(id):
    return Party.objects.get(id=id)

def get_requests_by_customer_id(id):
    customer = Customer.objects.get(id=id)
    return Request.objects.filter(customer = customer)

def get_request_by_id(id):
    return Request.objects.get(id=id)

def get_parties_by_customer_id(id):
    requests = get_requests_by_customer_id(id)
    all_parties = Party.objects.all()
    res = []
    for p in all_parties:
        if p.request in requests:
            res.append(p)
    return res

def get_party_by_request_id(id):
    request = get_request_by_id(id)
    return Party.objects.get(request = request)

def get_attend_request_by_id(id):
    return AttendRequest.objects.get(id=id)

def get_attend_requests_by_party_id(id):
    party = get_party_by_id(id)
    return AttendRequest.objects.filter(party = party)

def get_pending_attendees_by_customer_id(id):
    res = []
    parties = get_parties_by_customer_id(id)
    for p in parties:
        ats = get_attend_requests_by_party_id(p.id)
        for at in ats:
            if at.decision == 'PENDING':
                res.append(at.customer)
    return res

def get_pending_attend_requests_by_customer_id(id):
    res = []
    parties = get_parties_by_customer_id(id)
    ats = AttendRequest.objects.filter(decision = 'PENDING')
    for at in ats:
        if at.party in parties:
            res.append(at)
    return res

def get_accepted_attendees_by_party_id(id):
    attend_requests = get_attend_requests_by_party_id(id)
    res = []
    for ar in attend_requests:
        if ar.decision == 'ACCEPTED':
            res.append(ar.customer)
    return res

def has_made_an_attend_request(customer, party):
    res = False
    attend_requests = get_attend_requests_by_party_id(party.id)
    for ar in attend_requests:
        if ar.customer == customer:
            res = True
            break
    return res

def number_of_attendees_so_far(party):
    return AttendRequest.objects.filter(party = party, decision = 'ACCEPTED')