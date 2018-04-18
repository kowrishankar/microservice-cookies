from django.db import models


class ClickEvent(models.Model):
    click_url = models.CharField(max_length=200)
    uuid = models.CharField(max_length=200)
    time = models.CharField(max_length=200)
    epoch = models.FloatField()
    endpoint = models.CharField(max_length=200)