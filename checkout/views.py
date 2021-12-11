from django.shortcuts import render, get_object_or_404
from .models import Product
from django.contrib import messages

from .forms import OrderForm


def checkout(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'product': product,
    }

    return render(request, template, context)

def submit_order(request):

    form = OrderForm()
    if request.method == 'POST':
        print('Printing Post', request.POST)

    template = 'checkout/order_success.html'
    context = {'form': form}
    return render(request, template, context)