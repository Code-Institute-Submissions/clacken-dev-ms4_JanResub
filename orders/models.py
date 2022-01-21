import uuid

from django.db import models
from products.models import Product
from profiles.models import UserProfile


class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name='orders')
    date = models.DateTimeField(auto_now_add=True)
    service = models.ForeignKey(Product, null=False, blank=False,
                                on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=False,
                                default=0)
    description = models.TextField(null=False, blank=False)
    image = models.ImageField(null=True, blank=True)
    is_fulfilled = models.BooleanField(default=False)
    changes_requested = models.TextField(null=False, blank=True)

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()

        self.total = self.total
        super().save(*args, **kwargs)


class Testimonial(models.Model):
    """
    A model for testimonials to be shown and drawn from
    """
    customer_name = models.CharField(max_length=32, null=True)
    testimony = models.TextField(null=False, blank=False)
    product_purchased = models.ForeignKey(Product, on_delete=models.SET_NULL,
                                          null=True, blank=True,
                                          related_name='product')
 
    def __str__(self):
        return str(self.testimony)


