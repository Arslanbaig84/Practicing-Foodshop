# transactions/views.py
from django.shortcuts import render, get_object_or_404, redirect
from products.models import Product
from django.contrib.auth.decorators import login_required
from django.db import transaction
from .models import Cart, CartItem, Order, OrderItem
from .forms import FeedbackForm

@login_required(login_url="/users/login_user/")
def menu(request):
    products = Product.objects.all()
    return render(request, 'transactions/menu.html', {'products': products})


@login_required(login_url="/users/login_user/")
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, uid=product_id)
    
    # Try to get the existing active cart for the user
    try:
        cart = Cart.objects.get(user=request.user, is_active=True)
    except Cart.DoesNotExist:
        # No active cart found, so create a new one
        cart = Cart.objects.create(user=request.user, is_active=True)
    
    # Check if the product is already in the cart
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    
    if not created:
        # If the item already exists, just update the quantity
        cart_item.quantity += int(request.POST.get('quantity', 1))
        cart_item.save()
    else:
        # If the item is newly added, set the quantity
        cart_item.quantity = int(request.POST.get('quantity', 1))
        cart_item.save()
    
    return redirect('cart')  # or wherever you want to redirect after adding the item

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
        cart.delete()

    return render(request, "transactions/success.html", {'message': "Order placed successfully!"})


@login_required(login_url="/users/login_user/")
def contact(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)  # Don't save the form yet
            feedback.user = request.user  # Assign the current logged-in user
            feedback.save()  # Now save it with the user information            
            return redirect('menu')
    form = FeedbackForm()
    return render(request, "transactions/contact.html", {'form': form})


@login_required(login_url="/users/login_user/")
def order_status(request):
    orders = Order.objects.filter(user = request.user)
    return render(request, "transactions/order_status.html", {'orders': orders})