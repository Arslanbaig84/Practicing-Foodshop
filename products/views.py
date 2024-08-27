from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product, ProductImage

def product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.save()

            # Handle multiple file uploads
            files = request.FILES.getlist('images')
            for file in files:
                ProductImage.objects.create(product=product, product_images=file)

            return redirect('product/product.html')  # Replace 'success_url' with your success URL
    else:
        form = ProductForm()
        return render(request, 'products/product.html', {'form': form})