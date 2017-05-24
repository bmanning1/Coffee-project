from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Coffee
from django.utils import timezone


@login_required
def all_coffees(request):
    coffees = Coffee.objects.all()
    all_purcahses = request.user.purchases.all()
    number_purchases = len(all_purcahses)
    if number_purchases != 0:
        purchase = request.user.purchases.latest('subscription_end').coffee
        subscription_valid = request.user.purchases.latest('subscription_end').subscription_end > timezone.now()
        args = {"coffees": coffees, "subscription_valid": subscription_valid, "name": purchase.name}
    else:
        args = {"coffees": coffees, "subscription_valid": False, "name": None}
    return render(request, "coffees/coffees.html", args)


@login_required
def user_purchases(request):
    all_purcahses = request.user.purchases.all()
    number_purchases = len(all_purcahses)
    if number_purchases != 0:
        end_date = request.user.purchases.latest('subscription_end').subscription_end
        purchase = request.user.purchases.latest('subscription_end').coffee
        subscription_valid = request.user.purchases.latest('subscription_end').subscription_end > timezone.now()
        args = {'price': purchase.price, 'get': request.GET, 'name': purchase.name,
                'number_purchases': number_purchases, "subscription_valid": subscription_valid,
                "end_date": end_date, "coffees_left": int(purchase.name[0:2])-4}
    else:
        args = {'price': None, 'get': request.GET, 'name': None,
                'number_purchases': 0, "subscription_valid": False, "subscription_end_date": None, "coffees_left": 0}
    return render(request, "profile.html", args)


def get_price(request):
    coffees = Coffee.objects.all()
    return render(request, "price.html", {"coffees": coffees})
