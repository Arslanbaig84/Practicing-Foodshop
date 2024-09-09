from django.shortcuts import render, redirect
from .forms import CustomUserForm
from django.contrib.auth import update_session_auth_hash, authenticate, login, logout
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from .manager import UserManager

def register(request):
    if request.method == "POST":
        form = CustomUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('login_user')
        else:
            print("Form is invalid:", form.errors)
    else:
        form = CustomUserForm()
    return render(request, 'users/register.html', {'form': form})

@user_passes_test(lambda u: u.is_superuser)
def create_staff_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        UserManager().create_staffuser(email=email, password=password)
    return render(request, 'create_staff.html')

def login_user(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, email=email, password=password)
        if user:
            login(request, user)
            messages.success(request, "Login successful")
            return redirect(reverse('profile'))
        else:
            return render(request, 'users/login_user.html', {'message': "Invalid Email or Password"})
    return render(request, 'users/login_user.html')

@login_required(login_url="/users/login_user/")
def logout_user(request):
    logout(request)
    messages.success(request, "Logout successful")
    return render(request, "users/login_user.html")

@login_required(login_url="/users/login_user/")
def profile(request):
    return render(request, "users/profile.html")

@login_required(login_url="/users/login_user/")
def edit_profile(request):
    if request.method == "POST":
        form = CustomUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
        else:
            print(form.errors)
    else:
        form = CustomUserForm(instance=request.user)
    return render(request, 'users/edit_profile.html', {'form': form})
