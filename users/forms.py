from .models import CustomUser
from django import forms
from django.contrib.auth.forms import UserCreationForm

#creating custom user form 

class CustomUserForm(UserCreationForm):
    
    class Meta:
        model = CustomUser
        fields = fields = [
            'email',
            'first_name',
            'last_name',
            'contact',
            'password1',
            'password2'
        ]

