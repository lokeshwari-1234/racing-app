from django.shortcuts import render
from .models import Team, Driver, Race

def home(request):
    teams = Team.objects.all()
    drivers = Driver.objects.all()
    races = Race.objects.all()
    return render(request, 'home.html', {'teams': teams, 'drivers': drivers, 'races': races})

