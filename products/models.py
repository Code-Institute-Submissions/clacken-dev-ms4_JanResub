from django.db import models
from profiles.models import UserProfile


class Product(models.Model):
    """
    A model for the products available
    """
    service_type = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(null=True)

    def __str__(self):
        return str(self.service_type)


class Review(models.Model):
    """
    A model for the reviews of the workouts.
    """
    product = models.ForeignKey(
        Product, null=True, blank=True, on_delete=models.SET_NULL
    )
    user = models.ForeignKey(
        UserProfile, null=True, blank=True, on_delete=models.CASCADE
    )
    review_title = models.CharField(max_length=254, null=True, blank=True)
    review = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.review_title)