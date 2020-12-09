from dayssinceapi.models.DaysSinceUser import DaysSinceUser
from django.db import models

class Articles(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=200, default='none')
    link = models.CharField(max_length=5000, default='none')
    user = models.ForeignKey(DaysSinceUser, on_delete=models.CASCADE)
