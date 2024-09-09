
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .forms import ProductForm
from .models import Product, ProductImage
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/users/login_user/")
def product_form(request):
    user = request.user
    if user.is_staff:
        if request.method == 'POST':
            form = ProductForm(request.POST, request.FILES)
            if form.is_valid():
                product = form.save(commit=False)
                product.created_by = request.user
                product.save()

                # Handle multiple file uploads
                files = request.FILES.getlist('images')
                for file in files:
                    ProductImage.objects.create(product=product, image=file)

                return redirect('index')
            else:
                # If the form is invalid, return the form with errors
                return render(request, 'products/product_form.html', {'form': form})
        else:
            form = ProductForm()
            return render(request, 'products/product_form.html', {'form': form})

    

@login_required(login_url="/users/login_user/")
def index(request):
    products = Product.objects.filter(user=request.user)
    return render(request, "products/index.html", {'products':products})


@login_required(login_url="/users/login_user/")
def edit_product(request, product_id):
    user = request.user
    if user.is_staff:
        # Fetch the existing product instance
        product_instance = get_object_or_404(Product, uid=product_id)
        
        if request.method == "POST":
            # Pass the product_instance to the form to update it
            form = ProductForm(request.POST, request.FILES, instance=product_instance)
            if form.is_valid():
                # Save the form but don't commit (to add other fields)
                product = form.save(commit=False)
                product.created_by = request.user  # Assuming this is a field on the Product model
                product.save()

                # Handle multiple file uploads for the product
                files = request.FILES.getlist('images')
                for file in files:
                    ProductImage.objects.create(product=product, image=file)

                return redirect('index')  # Ensure 'index' is a valid URL name
        else:
            # On GET request, just pass the form pre-filled with the product instance
            form = ProductForm(instance=product_instance)

        # Render the edit product page
        return render(request, "products/edit_product.html", {'form': form, 'product_instance': product_instance})
    
    # If the user is not staff, redirect or return an error page
    return render(request, 'error.html', {'message': 'You are not authorized to edit products.'})