from django import forms, 
from products.models import Product
from .models import CartItem, FeedBack

class CartItemForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(CartItemForm, self).__init__(*args, **kwargs)
        products = Product.objects.all()
        for product in products:
            self.fields[f'product_{product.uid}'] = forms.BooleanField(
                label=product.product_name,
                required=False
            )
            self.fields[f'quantity_{product.uid}'] = forms.ChoiceField(
                choices=[(i, i) for i in range(1, 6)],
                label='Quantity',
                required=False
            )

    def save(self, user):
        """
        Custom save method to save selected products and their quantities to the database.
        """
        for field_name, value in self.cleaned_data.items():
            if field_name.startswith('product_') and value:
                product_id = field_name.split('_')[1]
                product = Product.objects.get(id=product_id)
                quantity = self.cleaned_data.get(f'quantity_{product_id}', 1)
                CartItem.objects.create(
                    product=product,
                    quantity=quantity,
                    created_by=user
                )

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = FeedBack
        fields = ['feedback']