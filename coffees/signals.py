import arrow
import models


def subscription_created(sender, **kwargs):
    # Subscription created signal
    ipn_obj = sender
    coffee_id = ipn_obj.custom.split('-')[0]
    user_id = ipn_obj.custom.split('-')[1]
    models.Purchase.objects.create(coffee_id=coffee_id,
                                   user_id=user_id,
                                   subscription_end=arrow.now().replace(weeks=+4).datetime)


def subscription_was_cancelled(sender, **kwargs):
    # Subscription cancelled signal
    ipn_obj = sender
    coffee_id = ipn_obj.custom.split('-')[0]
    user_id = ipn_obj.custom.split('-')[1]
    purchase = models.Purchase.object.get(user_id=user_id, coffee_id=coffee_id)
    purchase.subscription_end = arrow.now().datetime
    purchase.save()
