from django.shortcuts import render, get_object_or_404
from .models import Product
from django.contrib import messages
from django.conf import settings
import stripe

from .forms import OrderForm


def checkout(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

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
        'stripe_public_key': 'pk_test_51Ju1cJCVL6fX972lJGUEXagG6xY1kb1UqzZp8fiuHTtYnFNxOn3nzuOz37jP7YBCb8vfCXLzxSNnYVasbCmcQK1p00lE0hkIkq',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)

def submit_order(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    form = OrderForm()
    if request.method == 'POST':
        
        order_form = {
            'description': request.POST['description'],
        }

        form = OrderForm(order_form)
        if form.is_valid():
            order_form = form.save(commit=False)
            order_form.user = request.user.email
            order_form.service = product
            order_form.total = product.price
            form.save()
            messages.success(
                request, 'Your order has been created.')

            



    template = 'checkout/order_success.html'
    context = {'form': form}
    return render(request, template, context)