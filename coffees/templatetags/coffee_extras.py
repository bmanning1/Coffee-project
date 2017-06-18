import uuid
from django import template
from django.conf import settings
from paypal.standard.forms import PayPalPaymentsForm

register = template.Library()


# Paypal Form dependent on the User being subscribed already
def paypal_form_for(coffee, user):
    all_purcahses = user.purchases.all()
    number_purchases = len(all_purcahses)
    # If User Purchases is not empty and the latest Purchase is valid then User is Subscribed
    if number_purchases != 0:
        if user.purchases.order_by('subscription_created_date')[0].subscription_valid:
            html = "Subscribed!"
    # Paypal Dictionary
    else:
        paypal_dict = {
            "business": settings.PAYPAL_RECEIVER_EMAIL,
            "currency_code": "GBP",
            "cmd": "_xclick-subscriptions",
            "a3": coffee.price,
            "p3": 1,
            "t3": "M",
            "src": 1,
            "sra": 1,
            "item_name": coffee.name,
            "invoice": uuid.uuid4(),
            "notify_url": settings.PAYPAL_NOTIFY_URL,
            "return_url": "%s/paypal-return/" % settings.SITE_URL,
            "cancel_return": "%s/paypal-cancel/" % settings.SITE_URL,
            "custom": "%s-%s" % (coffee.pk, user.id)
        }

        if settings.DEBUG:
            html = PayPalPaymentsForm(initial=paypal_dict, button_type='subscribe').sandbox()
        else:
            html = PayPalPaymentsForm(initial=paypal_dict, button_type='subscribe').render()

    return html


register.simple_tag(paypal_form_for)
