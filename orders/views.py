from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from profiles.models import UserProfile
from .models import Order
from .forms import OrderForm

# Create your views here.


@login_required
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


@login_required
def update_order(request, order_number):
    """ A view to add the finished graphics to an order """

    order = get_object_or_404(Order, order_number=order_number)
    form = OrderForm(instance=order)

    context = {
        'order': order,
        'form': form
    }

    template = 'orders/update_order.html'

    return render(request, template, context)


@login_required
def edit_order(request, order_number):
    """ Edit a graphic by adding image and updating the instance """
    order = get_object_or_404(Order, order_number=order_number)
    if request.method == 'POST':
        form = OrderForm(request.POST, request.FILES, instance=order)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('orders'))
        else:
            messages.error(request, 'Failed to update product.\
                          Please ensure the form is valid.')
    else:
        form = OrderForm(instance=order)
        messages.info(request, f'You are editing {order_number}')

    template = 'orders/update_order.html'
    context = {
        'form': form,
        'order': order,
    }

    return render(request, template, context)
