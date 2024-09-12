# transactions/views.py
from django.shortcuts import render, get_object_or_404, redirect
from products.models import Product
from django.contrib.auth.decorators import login_required
from django.db import transaction
from .models import Cart, CartItem, Order, OrderItem, FeedBack
from .forms import FeedbackForm

@login_required(login_url="/users/login_user/")
def menu(request):
    products = Product.objects.all()
    return render(request, 'transactions/menu.html', {'products': products})

@login_required(login_url="/users/login_user/")
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, uid=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)

    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
    cart_item.save()

    return redirect('cart')

@login_required(login_url="/users/login_user/")
def cart(request):
    cart = get_object_or_404(Cart, user=request.user)
    if cart.is_active == True:
        cart_items = CartItem.objects.filter(cart=cart)
        cart_price = Cart.total_price(cart)
        return render(request, 'transactions/cart.html', {'cart': cart, 'cart_items': cart_items, 'cart_price':cart_price})
    return render(request, "transactions/cart.html", {'cart': None, 'cart_items': [], 'cart_price': "Nill"})


@login_required(login_url="/users/login_user/")
def success(request):
    # Ensure the user is authenticated
    user = request.user

    # Getting the cart for the user
    cart = get_object_or_404(Cart, user=user, is_active=True)
    cart_items = CartItem.objects.filter(cart=cart)
    
    if not cart_items.exists():
        return render(request, "transactions/success.html", {'message': "Cart is empty!"})

    # Create new order
    with transaction.atomic():
        new_order = Order.objects.create(
            user=user,
            total_price=cart.total_price(),  # Total price from cart
            shipping_address=request.POST.get('shipping_address')  # shipping address from FE
        )

        # Creating order items for the order
        for cart_item in cart_items:
            OrderItem.objects.create(
                order=new_order,
                product=cart_item.product,
                quantity=cart_item.quantity,
                price=cart_item.product.product_price
            )

        # Making cart inactive
        cart.is_active = False
        cart.save()

        # Remove cart items
        cart_items.delete()

    return render(request, "transactions/success.html", {'message': "Order placed successfully!"})

@login_required(login_url="/users/login_user/")
def contact(request):
    form = FeedbackForm()
    return render(request, "transactions/contact.html", {'form': form})