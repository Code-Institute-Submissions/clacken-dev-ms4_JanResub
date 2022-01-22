from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<product_id>', views.product_detail, name='product_detail'),
    path('edit/<product_id>/', views.edit_product, name='edit_product'),
    path('add_review/<product_id>/', views.add_review, name='add_review'),
]