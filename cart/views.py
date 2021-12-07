from django.shortcuts import render, get_object_or_404
from products.models import Product
# Create your views here.

def order(request, product_id):
    """ Create an order form for a product which can be sent to checkout """
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }


    return render(request, 'cart/cart.html', context)

    