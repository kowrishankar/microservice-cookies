from django.db import models

# Create your models here.

class Account(models.Model):
    username = models.CharField(max_length=200)
    enabled_tracking = models.BooleanField()