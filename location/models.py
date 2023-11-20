from django.db import models
from user.models import User


class Location(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
