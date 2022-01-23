from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('request_changes/<order_number>', views.request_changes, name='request_changes'),
]