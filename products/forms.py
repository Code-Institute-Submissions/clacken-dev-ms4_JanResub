from django import forms
from .models import Review 

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ("user", "product", "date")
        fields = ("review_title", "review")