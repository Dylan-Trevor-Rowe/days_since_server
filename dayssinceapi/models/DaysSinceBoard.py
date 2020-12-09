from dayssinceapi.models.DaysSinceUser import DaysSinceUser
from django.db import models


class DaysSinceBoard(models.Model):
    daysSinceBoard = models.IntegerField()
    user = models.ForeignKey(DaysSinceUser, on_delete=models.CASCADE)