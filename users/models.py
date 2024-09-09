from django.contrib.auth.models import AbstractUser
import uuid
from django.db import models
from .manager import UserManager

class CustomUser(AbstractUser):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    username = None  # Explicitly remove the username field
    email = models.EmailField(unique=True, null=False, blank=False)
    contact = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['contact']

    objects = UserManager()  # Make sure your custom manager is set here
