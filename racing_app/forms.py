from django import forms
from .models import Team, Driver, Race

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = '__all__'

class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ['first_name','last_name','dob','team']

class RaceForm(forms.ModelForm):
    class Meta:
        model = Race
        fields = '__all__'
