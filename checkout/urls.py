from django.urls import path
from . import views

urlpatterns = [
    
    path('checkout/<product_id>/', views.checkout, name='checkout'),
    path('submit_order/', views.submit_order, name='submit_order'),
]