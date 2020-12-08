from dayssinceapi.models.DaysSinceUser import DaysSinceUser
from django.contrib.auth.models import User
from django.db import models
from django.core.exceptions import ValidationError
from django.db.models.signals import pre_save
from django.dispatch import receiver

class DaysSinceBoard(models.Model):
    days_since_board = models.IntegerField()
    user = models.ForeignKey(DaysSinceUser, on_delete=models.CASCADE)