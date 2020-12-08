from dayssinceapi.models.DaysSinceUser import DaysSinceUser
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.db import models

class Goals(models.Model):
    date = models.DateField()
    goal_name = models.CharField(max_length=200, default='none')
    user = models.ForeignKey(DaysSinceUser, on_delete=models.CASCADE)
  