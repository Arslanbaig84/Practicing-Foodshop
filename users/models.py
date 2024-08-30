from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from .manager import UserManager

# Create your models here.
class CustomUser(AbstractUser):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    username = None
    email = models.EmailField(unique=True, null=False, blank=False)
    contact = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['contact']

    objects = UserManager()  # Make sure your custom manager is set here