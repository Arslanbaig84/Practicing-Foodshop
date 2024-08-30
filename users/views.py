from django.shortcuts import render, redirect
from .forms import CustomUserForm
from django.contrib.auth import update_session_auth_hash, authenticate, login, logout

# Create your views here.
def register(request):
    if request.method == "POST":
        form = CustomUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('register')
    form = CustomUserForm()
    return render(request, 'users/register.html', {'form':form})


def login_user(request):
    if request.method == "POST":
        username = request.POST["email"]
        password = request.POST["password"]
        print(f"Username: {username}, Password: {password}")
        user = authenticate(request, username = username, password = password)
        if user:
            login(request, user)
            return redirect('products/product_form')
        else:
            return render(request, 'users/login_user.html', {'message': "Invalid Username or Password"})
    return render(request, 'users/login_user.html')