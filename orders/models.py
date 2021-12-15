from django.db import models
from profiles.models import UserProfile

# Create your models here.
class Testimonial(models.Model):
    """
    A model for testimonials to be shown and drawn from
    """
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    testimony = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.testimony


