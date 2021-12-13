from django.urls import path
from . import views

urlpatterns = [
    
    path('checkout/<product_id>/', views.checkout, name='checkout'),
    path('checkout_success/<order_number>', views.checkout_success, name='checkout_success'),
    path('order_now/<product_id>', views.order_now, name='order_now'),
]