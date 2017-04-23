from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Coffee


@login_required
def all_coffees(request):
    coffees = Coffee.objects.all()
    return render(request, "coffees/coffees.html", {"coffees": coffees})

def get_price(request):
    coffees = Coffee.objects.all()
    return render(request, "price.html", {"coffees": coffees})
