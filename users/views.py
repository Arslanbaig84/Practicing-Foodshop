from django.shortcuts import render, redirect
from .forms import CustomUserForm
from django.contrib.auth import update_session_auth_hash, authenticate, login, logout
from django.urls import reverse
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == "POST":
        form = CustomUserForm(request.POST)
        if form.is_valid():
            user = form.save()
#            print("User created:", user)
            update_session_auth_hash(request, user)  # Optional, usually for password updates
            return redirect('login_user')  # Redirect to login or another page
        else:
            print("Form is invalid:", form.errors)  # Print errors for debugging
    else:
        form = CustomUserForm()
        return render(request, 'users/register.html', {'form': form})

def login_user(request):
    if request.method == "POST":
        username = request.POST["email"]
        password = request.POST["password"]
#        print(f"Username: {username}, Password: {password}")
        user = authenticate(request, username = username, password = password)
#        print(user)

        if user:
            login(request, user)
            messages.success(request, "Login successful")
            return redirect(reverse('product_form'))
        else:
            return render(request, 'users/login_user.html', {'message': "Invalid Username or Password"})
    return render(request, 'users/login_user.html')


def logout_user(request):
    logout(request)
    messages.success(request, "Logout successful")
    return render(request, "users/login_user.html")