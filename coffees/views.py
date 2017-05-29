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
        purchase = request.user.purchases.latest('subscription_created_date')
        args = {"coffees": coffees, "subscription_valid": purchase.subscription_valid, "name": purchase.coffee.name}
    else:
        args = {"coffees": coffees, "subscription_valid": False, "name": None}
    return render(request, "coffees/coffees.html", args)


@login_required
def user_purchases(request):
    all_purcahses = request.user.purchases.all()
    number_purchases = len(all_purcahses)
    first_login = request.user.date_joined > timezone.now() - timezone.timedelta(minutes=30)

    if number_purchases != 0:
        purchase = request.user.purchases.latest('subscription_created_date')
        a = purchase.subscription_created_date
        b = timezone.now()
        renewal_date = (a-b).days%30

        args = {'price': purchase.coffee.price, 'get': request.GET, 'name': purchase.coffee.name,
                'number_purchases': number_purchases, "subscription_valid": purchase.subscription_valid,
                "renewal_date": renewal_date, "coffees_left": int(purchase.coffee.name[0:2]) - 4, 'first_login': first_login}
    else:
        args = {'price': None, 'get': request.GET, 'name': None,
                'number_purchases': 0, "subscription_valid": False, "renewal_date": None, "coffees_left": 0,
                'first_login': first_login}

    return render(request, "Profile/profile.html", args)


def get_price(request):
    coffees = Coffee.objects.all()
    return render(request, "price.html", {"coffees": coffees})
