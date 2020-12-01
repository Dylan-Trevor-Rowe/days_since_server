from django.core.exceptions import ValidationError
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.db import models

Logged_Symptoms = (
    ('none','headache'),
    ('nausea', 'vertigo'),
    ('blurred vison','RED'),
    ('orange','ORANGE'),
    ('black','BLACK'),
)

class WellBeing(models.Model):
    """Representation of a playable game that a gamer can create"""
    date = models.DateField()
    fatigueScale = models.IntegerField()
    painScale = models.IntegerField()
    symptoms = models.CharField(max_length=30, choices= Logged_Symptoms, default='none')
    hoursOfSleep = models.IntegerField()
    emotionalWellBeing = models.CharField(max_length=50)