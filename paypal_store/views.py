from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@csrf_exempt
@login_required
def paypal_return(request):
    print request.POST

    purchase = request.user.purchases.order_by('subscription_created_date')[0].coffee
    args = {'price': purchase.price, 'get': request.GET, 'name': purchase.name}
    return render(request, 'paypal/paypal_return.html', args)


def paypal_cancel(request):
    args = {'post': request.POST, 'get': request.GET}
    return render(request, 'paypal/paypal_cancel.html', args)
