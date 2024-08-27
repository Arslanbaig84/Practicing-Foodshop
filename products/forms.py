from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    images = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': False}), required=True)

    class Meta:
        model = Product
        fields = ['product_name', 'product_slug', 'product_description', 'product_price']
        labels = {
            'product_name': 'Product Name',
            'product_slug': 'Slug',
            'product_description': 'Description',
            'product_price': 'Price'
        }
        help_texts = {
            'product_slug': 'Enter a unique slug for the product.',
        }