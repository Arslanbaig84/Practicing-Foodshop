# transactions/views.py
from django.shortcuts import render, redirect
from .forms import CartItemForm
from .models import CartItem
from products.models import Product
from django.contrib.auth.decorators import login_required


@login_required
def menu(request):
    if request.method == 'POST':
        pass
    else:
        form = CartItemForm()

    return render(request, 'transactions/menu.html', {'form': form})
