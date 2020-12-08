from dayssinceapi.models import DaysSinceUser
from dayssinceapi.models.Articles import Articles
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.db import models

class Comments(models.Model):
    comment = models.CharField(max_length=10000, default='none')
    user = models.ForeignKey(DaysSinceUser, on_delete=models.CASCADE)
    articleid = models.ForeignKey(Articles, on_delete=models.CASCADE)
