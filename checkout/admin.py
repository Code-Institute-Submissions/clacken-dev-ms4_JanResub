from django.contrib import admin
from .models import Order


class OrderAdmin(admin.ModelAdmin):

    readonly_fields = ('order_number', 'date',
                       'total',)

    fields = ('order_number', 'date', 'user',
              'email', 'service', 'total',
              'description', 'image',)

    list_display = ('order_number', 'date', 'user',
              'email', 'service', 'total',
              'description', 'image',)

    ordering = ('-date',)

admin.site.register(Order)