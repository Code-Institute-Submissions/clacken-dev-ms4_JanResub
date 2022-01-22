from django import forms
from .models import Review, Product

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ("user", "product", "date")
        fields = ("review_title", "review")


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        # Include all the fields from the model
        fields = "__all__"