from django.shortcuts import render, redirect, get_object_or_404
from .models import Team, Driver, Race
from .forms import TeamForm, DriverForm, RaceForm


# HOME
def home(request):
    return render(request, 'home.html')

# TEAM CRUD

def team_list(request):
    teams = Team.objects.all()
    return render(request, 'team_list.html', {'teams': teams})

def team_create(request):
    form = TeamForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('team_list')
    return render(request, 'team_form.html', {'form': form})

def team_edit(request, pk):
    team = get_object_or_404(Team, pk=pk)
    form = TeamForm(request.POST or None, request.FILES or None, instance=team)
    if form.is_valid():
        form.save()
        return redirect('team_list')
    return render(request, 'team_form.html', {'form': form})

def team_delete(request, pk):
    team = get_object_or_404(Team, pk=pk)
    if request.method == 'POST':
        team.delete()
        return redirect('team_list')
    return render(request, 'confirm_delete.html', {'object': team, 'type': 'Team'})

# DRIVER CRUD

def driver_list(request):
    drivers = Driver.objects.all()
    return render(request, 'driver_list.html', {'drivers': drivers})

def driver_create(request):
    form = DriverForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('driver_list')
    return render(request, 'driver_form.html', {'form': form})

def driver_edit(request, pk):
    driver = get_object_or_404(Driver, pk=pk)
    form = DriverForm(request.POST or None, instance=driver)
    if form.is_valid():
        form.save()
        return redirect('driver_list')
    return render(request, 'driver_form.html', {'form': form})

def driver_delete(request, pk):
    driver = get_object_or_404(Driver, pk=pk)
    if request.method == 'POST':
        driver.delete()
        return redirect('driver_list')
    return render(request, 'confirm_delete.html', {'object': driver, 'type': 'Driver'})

# RACE CRUD

def race_list(request):
    races = Race.objects.all()
    return render(request, 'race_list.html', {'races': races})

def race_create(request):
    form = RaceForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('race_list')
    return render(request, 'race_form.html', {'form': form})

def race_edit(request, pk):
    race = get_object_or_404(Race, pk=pk)
    form = RaceForm(request.POST or None, instance=race)
    if form.is_valid():
        form.save()
        return redirect('race_list')
    return render(request, 'race_form.html', {'form': form})

def race_delete(request, pk):
    race = get_object_or_404(Race, pk=pk)
    if request.method == 'POST':
        race.delete()
        return redirect('race_list')
    return render(request, 'confirm_delete.html', {'object': race, 'type': 'Race'})


from rest_framework import viewsets
from .models import Team, Driver, Race
from .serializers import TeamSerializer, DriverSerializer, RaceSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer

class RaceViewSet(viewsets.ModelViewSet):
    queryset = Race.objects.all()
    serializer_class = RaceSerializer