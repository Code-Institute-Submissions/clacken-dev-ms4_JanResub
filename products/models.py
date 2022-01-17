from django.db import models


class Product(models.Model):
    service_type = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(null=True)

    def __str__(self):
        return str(self.service_type)
