from django.db import models
from products.models import Product
from users.models import CustomUser
import uuid

# Create your models here.
class CartBaseModel(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='cart')

    class Meta:
        abstract = True #To make sure that django treats it as a class and not a model and doesn't create a table name BaseProductModel

class CartItem(CartBaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.product.product_name
    
    def get_price(self):
        return self.product.product_price * self.quantity
    