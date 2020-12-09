from django.db import models
from django.contrib.auth.models import User



class DaysSinceUser(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)

@property
def fullname(self):
        return f"{self.user.firstName} {self.user.lastName}"

@property
def username(self):
        return f"{self.user.username}"
