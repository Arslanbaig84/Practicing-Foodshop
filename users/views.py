from django.shortcuts import render, redirect
from .forms import CustomUserForm
from django.contrib.auth import update_session_auth_hash

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