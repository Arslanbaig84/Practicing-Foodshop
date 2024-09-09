from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib import messages
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    # Set the ordering to 'email' instead of 'username'
    ordering = ['email']

    # Define the fieldsets, including the 'Important dates' section
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'contact')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),  # Add the important dates section
    )

    # Exclude non-editable fields from the form
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if not request.user.is_superuser:
            # Prevent non-superusers from even seeing 'is_staff' and 'is_superuser' fields
            form.base_fields.pop('is_staff', None)
            form.base_fields.pop('is_superuser', None)
        # Remove non-editable fields from the form
        form.base_fields.pop('created_at', None)
        form.base_fields.pop('updated_at', None)
        return form

    def save_model(self, request, obj, form, change):
        # Only allow superusers to create or modify staff or superusers
        if not request.user.is_superuser and ('is_staff' in form.cleaned_data or 'is_superuser' in form.cleaned_data):
            messages.error(request, "You do not have permission to modify staff or superuser status.")
            return  # Prevent saving if not a superuser
        super().save_model(request, obj, form, change)

# Register your custom admin class
admin.site.register(CustomUser, CustomUserAdmin)
