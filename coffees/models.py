from datetime import timedelta

from django.db import models
from django.conf import settings
from django.utils import timezone


class Coffee(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        app_label = "coffees"

    def __unicode__(self):
        return self.name


class Purchase(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='purchases')
    coffee = models.ForeignKey(Coffee)
    subscription_end = models.DateTimeField(default=timezone.now())

    class Meta:
        app_label = "coffees"


def get_subscription_end_date():
    timezone.now() + timedelta(30)
