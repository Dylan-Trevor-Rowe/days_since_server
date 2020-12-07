from dayssinceapi.models.DaysSinceUser import DaysSinceUser
from django.db import models
from django.contrib.auth.models import User

class JournalEntry(models.Model):
    date = models.DateField()
    entry = models.CharField(max_length=50000, default='none')
    user = models.ForeignKey(DaysSinceUser, on_delete=models.CASCADE, related_name='journalEntry')