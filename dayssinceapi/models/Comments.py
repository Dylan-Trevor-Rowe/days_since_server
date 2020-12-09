from dayssinceapi.models import DaysSinceUser
from dayssinceapi.models.Articles import Articles
from django.db import models

class Comments(models.Model):
    comment = models.CharField(max_length=10000, default='none')
    user = models.ForeignKey(DaysSinceUser, on_delete=models.CASCADE)
    article = models.ForeignKey(Articles, on_delete=models.CASCADE)
