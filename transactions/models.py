from django.db import models
from products.models import Product
from users.models import CustomUser
import uuid

# Create your models here.
class Cart(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='cart')

    def __str__(self):
        return f"{self.created_by.email} Cart"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.product.product_name
    
    def get_price(self):
        return self.product.product_price * self.product.meta_info.product_quantity
    