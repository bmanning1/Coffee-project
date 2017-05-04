from django.shortcuts import render

# Create your views here.
def get_index(request):
    return render(request, 'index.html')


def get_about(request):
    return render(request, 'About.html')


def get_contact(request):
    return render(request, 'contact.html')

# def get_price(request):
  #   coffees = Coffee.objects.all()
    # return render(request, "coffees/price.html", {"coffees": coffees})
