from dayssinceapi.models.DaysSinceUser import DaysSinceUser
from dayssinceapi.models.Goals import Goals
from django.contrib.auth.models import User
from django.db import models


class CheckedGoals(models.Model):
 user = models.ForeignKey("DaysSinceUser", on_delete=models.CASCADE)
 date = models.DateField()
 checked = models.BooleanField(default='false')
 goal = models.ForeignKey("Goals", on_delete=models.CASCADE)