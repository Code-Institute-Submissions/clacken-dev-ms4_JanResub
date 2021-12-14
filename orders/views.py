from django.shortcuts import render, get_object_or_404

from profiles.models import UserProfile
from checkout.models import Order

# Create your views here.
def orders(request):
    """ A view to return the orders page """
    profile = get_object_or_404(UserProfile, user=request.user)
    orders = Order.objects.all()

    template = 'orders/orders.html'
    context = {
        'profile': profile,
        'orders': orders,
    }
    

    return render(request, template, context)