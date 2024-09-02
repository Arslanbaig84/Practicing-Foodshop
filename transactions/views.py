"""from django.shortcuts import render, redirect
from .forms import CartItemForm

def menu(request):
    if request.method == 'POST':
        form = CartItemForm(request.POST)
        if form.is_valid():
            form.save(request.user)
            return redirect('cart')  # Redirect to your cart or another relevant page
    else:
        form = CartItemForm()

    return render(request, 'transactions/menu.html', {'form': form})"""

# transactions/views.py
from django.shortcuts import render, get_object_or_404, redirect
from products.models import Product
from .models import CartItem

def menu(request):
    if request.method == "POST":
        pass
        product = get_object_or_404(Product, id=product_id)
        ordered_quantity = int(request.POST.get('quantity', 1))

        # Create or update the CartItem for the selected product
        cart_item, created = CartItem.objects.get_or_create(product=product)
        cart_item.ordered_quantity += ordered_quantity
        cart_item.save()

        return redirect('menu')  # Redirect back to the menu after adding to the cart

    products = Product.objects.all()
    return render(request, 'transactions/menu.html', {'products': products})
