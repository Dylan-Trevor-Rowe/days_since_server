from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from django.db.models.signals import pre_save
from django.dispatch import receiver



class DaysSinceUser(models.Model):
    """Gamer model class"""
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
