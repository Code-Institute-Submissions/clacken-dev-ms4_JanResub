from django.db import models
from profiles.models import UserProfile

# Create your models here.
class Testimonial(models.Model):
    """
    A user profile model for maintaining default
    delivery information and order history
    """
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    testimony = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.testimony


class GalleryImage(models.Model):
    """
    A model for storing images used to display on the gallery page
    """
    
    image = models.ImageField(null=False, blank=False)

    def __str__(self):
        return self.image