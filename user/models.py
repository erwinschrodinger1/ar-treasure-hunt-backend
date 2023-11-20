from django.db import models


class User(models.Model):
    code = models.CharField(max_length=6)
