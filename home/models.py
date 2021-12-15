from django.db import models

# Create your models here.
class Image(models.Model):
    """
    An image model for gallery display
    """
    gallery_image = models.TextField(null=False, blank=False)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
