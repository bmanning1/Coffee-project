from django.db import models
from django.conf import settings
from django.utils import timezone
from signals import subscription_created, subscription_was_cancelled
from paypal.standard.ipn.signals import valid_ipn_received


def get_subscription_end_date():
    """ Used in a later model for a subscription created date """
    return timezone.now()


class Coffee(models.Model):
    """ Coffee model with Name, Description and Price options """
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        app_label = "coffees"

    def __unicode__(self):
        return self.name


class Purchase(models.Model):
    """ Purchase model with The User who is purchasing, type of Coffee subscription, 
    Purchase date and if the subscription is valid """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='purchases')
    coffee = models.ForeignKey(Coffee)
    subscription_created_date = models.DateTimeField(default=get_subscription_end_date)
    # When user elects to cancel, this becomes false
    subscription_valid = models.BooleanField(default=True)

    class Meta:
        app_label = "coffees"


valid_ipn_received.connect(subscription_created)
valid_ipn_received.connect(subscription_was_cancelled)
