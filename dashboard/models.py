from django.db import models
from building.models import Building
from party.models import Request, AttendRequest

# Create your models here.

def get_percentage_buildings(decision):
    all_buildings = Building.objects.all()
    buildings = Building.objects.filter(decision=decision)
    return (buildings.count()/all_buildings.count())*100

def get_percentage_party_requests(decision):
    all_party_requests = Request.objects.all()
    party_requests = Request.objects.filter(decision=decision)
    return (party_requests.count()/all_party_requests.count())*100

def get_percentage_attend_requests(decision):
    all_attend_requests = AttendRequest.objects.all()
    attend_requests = AttendRequest.objects.filter(decision=decision)
    return (attend_requests.count()/all_attend_requests.count())*100