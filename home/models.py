from django.db import models

# Create your models here.


class Image(models.Model):
    """
    An image model for gallery display
    """
    image = models.ImageField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
