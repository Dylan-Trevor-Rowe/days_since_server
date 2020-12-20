from dayssinceapi.models.DaysSinceUser import DaysSinceUser
from django.db import models

class Goals(models.Model):
    date = models.DateField()
    goal_name = models.CharField(max_length=200, default='none')
    goal_length = models.CharField(max_length=200, default='none')
    goal_reason = models.CharField(max_length=200, default='none')
    user = models.ForeignKey(DaysSinceUser, on_delete=models.CASCADE)
  