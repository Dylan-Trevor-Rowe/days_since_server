from django.db.models.fields import BooleanField
from dayssinceapi.models.DaysSinceUser import DaysSinceUser
from django.db import models

class Goals(models.Model):
    date = models.DateField()
    goal_name = models.BooleanField(default='false')
    user = models.ForeignKey(DaysSinceUser, on_delete=models.CASCADE)
  