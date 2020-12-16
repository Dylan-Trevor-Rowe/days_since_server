from dayssinceapi.models.DaysSinceUser import DaysSinceUser
from django.db import models


class DaysSinceBoard(models.Model):
    daysSinceBoard = models.IntegerField()
    created = models.DateField()
    user = models.ForeignKey(DaysSinceUser, on_delete=models.CASCADE)