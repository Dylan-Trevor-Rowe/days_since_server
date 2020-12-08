from dayssinceapi.models.DaysSinceUser import DaysSinceUser
from django.db import models


class WellBeing(models.Model):
    date = models.DateField()
    fatigueScale = models.IntegerField()
    painScale = models.IntegerField()
    symptoms = models.CharField(max_length=30, default='none')
    hoursOfSleep = models.IntegerField()
    emotionalWellBeing = models.IntegerField()
   