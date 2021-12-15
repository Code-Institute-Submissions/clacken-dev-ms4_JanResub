from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.orders, name='orders'),
    path('edit_order/<order_number>', views.edit_order, name='edit_order'),
]