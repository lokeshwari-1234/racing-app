from django.db import models
from django.core.exceptions import ValidationError
import datetime

def validate_image_size(image):
    if image.size > 50 * 1024:
        raise ValidationError("Image size must be less than 50KB")

def validate_dob(value):
    if value > datetime.date(2000, 12, 31):
        raise ValidationError("DOB must be before 31-12-2000")

def validate_future_date(value):
    if value <= datetime.date.today():
        raise ValidationError("Race date must be a future date")

def validate_past_date(value):
    if value and value >= datetime.date.today():
        raise ValidationError("Closure date must be in the past")

class Team(models.Model):
    team_name = models.CharField(max_length=256, unique=True)
    team_location = models.CharField(max_length=100)
    team_logo = models.ImageField(upload_to='team_logos/', validators=[validate_image_size])
    team_description = models.TextField(max_length=1024, blank=True, null=True)

    def __str__(self):
        return self.team_name

    def delete(self, *args, **kwargs):
        if self.driver_set.exists():
            raise ValidationError("Cannot delete team with registered drivers.")
        super().delete(*args, **kwargs)

class Driver(models.Model):
    first_name = models.CharField(max_length=96)
    last_name = models.CharField(max_length=96)
    dob = models.DateField(validators=[validate_dob])
    team = models.ForeignKey(Team, on_delete=models.PROTECT)
    races = models.ManyToManyField('Race', related_name='drivers_registered', blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def delete(self, *args, **kwargs):
        if self.races.exists():
            raise ValidationError("Cannot delete driver registered in races.")
        super().delete(*args, **kwargs)

class Race(models.Model):
    race_track_name = models.CharField(max_length=256, unique=True)
    track_location = models.CharField(max_length=100)
    race_date = models.DateField(validators=[validate_future_date])
    registration_closure_date = models.DateField(blank=True, null=True, validators=[validate_past_date])
    registered_drivers = models.ManyToManyField(Driver, related_name='registered_races', blank=True)

    def __str__(self):
        return self.race_track_name

    def delete(self, *args, **kwargs):
        if self.registered_drivers.exists():
            raise ValidationError("Cannot delete race with registered drivers.")
        super().delete(*args, **kwargs)

