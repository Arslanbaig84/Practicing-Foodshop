# transactions/forms.py
from django import forms
from products.models import Product
from .models import CartItem

class CartItemForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = ['products', 'quantity']
    
    # Override the default field definitions
    products = forms.ModelMultipleChoiceField(
        queryset=Product.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
        label='Select Products'
    )
    quantity = forms.ChoiceField(
        choices=[(i, i) for i in range(1, 6)],
        label='Quantity'
    )
