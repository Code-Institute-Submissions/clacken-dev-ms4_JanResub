from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .forms import OrderForm
from .models import Product, Order
from profiles.models import UserProfile

import stripe

@login_required
def checkout(request, product_id):
    """ A view to show the checkout page for an item and handle payments """ 
    product = get_object_or_404(Product, pk=product_id)

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    
    if request.method == 'POST':
        print("post request method executed")
        print(stripe_public_key)
        
        form_data = {
            'description': request.POST['description'],
        }

        order_form = OrderForm(form_data)
        profile = UserProfile.objects.get(user=request.user)

        if order_form.is_valid():
            order = order_form.save(commit=False)
            
            form_data = order_form.save(commit=False)
            form_data.user_profile = profile
            form_data.service = product
            form_data.total = product.price
            
            order.save()
            
            messages.success(
                request, 'Your order has been created.')
        return redirect(reverse('checkout_success', args=[order.order_number]))
    else:
        stripe_total = round(product.price * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )
        order_form = OrderForm()
    
    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'product': product,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


@login_required
def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to your email.')

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)