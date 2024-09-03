# transactions/views.py
from django.shortcuts import render, get_object_or_404, redirect
from products.models import Product
from .models import CartItem, Cart

def menu(request):
    products = Product.objects.all()
    return render(request, 'transactions/menu.html', {'products': products})


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, uid=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)

    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
    cart_item.save()

    return redirect('cart')

def cart(request):
    cart = get_object_or_404(Cart, user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    return render(request, 'transactions/cart.html', {'cart': cart, 'cart_items': cart_items})