from django import forms
from .models import Product

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['product_name', 'product_slug', 'product_description', 'product_price', 'product_availability']

    images = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': False}), required=False)