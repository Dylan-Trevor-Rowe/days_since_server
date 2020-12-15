from dayssinceapi.models.DaysSinceUser import DaysSinceUser
from django.db import models


class WellBeing(models.Model):
    date = models.DateField()
    fatigueScale = models.IntegerField()
    painScale = models.IntegerField()
    noSymptoms = models.BooleanField(default='false')
    numbness = models.BooleanField(default='false')
    tingling = models.BooleanField(default='false')
    # weakness = models.BooleanField(default='false')
    # stiffness = models.BooleanField(default='false')
    # coordinationOrBalanceProblems = models.BooleanField(default='false')
    # heatSensitivity = models.BooleanField(default='false')
    # incontenance = models.BooleanField(default='false')
    # brainFog = models.BooleanField(default='false')
    hoursOfSleep = models.IntegerField()
    emotionalWellBeing = models.IntegerField()
   