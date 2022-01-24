from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import UserProfile
from orders.models import Order
from .forms import OrderForm


def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'profile': profile,
        'orders': orders,
    }

    return render(request, template, context)


@login_required
def request_changes(request, order_number):
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

    template = 'profiles/change_order.html'
    context = {
        'form': form,
        'order': order,
    }

    return render(request, template, context)