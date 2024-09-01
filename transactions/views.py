from django.shortcuts import render, redirect
from .forms import CartItemForm

def menu(request):
    if request.method == 'POST':
        form = CartItemForm(request.POST)
        if form.is_valid():
            form.save(request.user)
            return redirect('cart')  # Redirect to your cart or another relevant page
    else:
        form = CartItemForm()

    return render(request, 'transactions/menu.html', {'form': form})
