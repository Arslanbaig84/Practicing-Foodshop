
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ProductForm
from .models import Product, ProductImage
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/users/login_user/")
def product_form(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.save()

            # Handle multiple file uploads
            files = request.FILES.getlist('images')
            for file in files:
                ProductImage.objects.create(product=product, image=file)

            return redirect(reverse('product_form'))
    else:
        form = ProductForm()

        return render(request, 'products/product_form.html', {'form': form})
