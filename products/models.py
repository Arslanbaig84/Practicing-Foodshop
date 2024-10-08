from django.db import models
import uuid
from users.models import CustomUser

UNITS = [('g', 'g'), ('Kg', 'Kg'), ('ml', 'ml'), ('l', 'l')]
AVAILABILITY = [('breakfast', 'breakfast'), ('lunch', 'lunch'), ('dinner', 'dinner'), ('full_day', 'full_day')]

# Create your models here.
class BaseProductModel(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='%(class)s_created')

    class Meta:
        abstract = True #To make sure that django treats it as a class and not a model and doesn't create a table name BaseProductModel


class Product(BaseProductModel):
    product_name = models.CharField(max_length=100)
    product_slug = models.SlugField(unique=True)
    product_description = models.TextField(max_length=500)
    product_price = models.PositiveIntegerField()
    product_availability = models.CharField(max_length=50, choices=AVAILABILITY, default='full_day')

    def __str__(self):
        return self.product_name


class ProductMeta(BaseProductModel):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name="meta_info")
    product_quantity = models.CharField(null=True, blank=True, max_length=10)
    measurement = models.CharField(choices=UNITS, null=True, blank=True, max_length=10)
    is_restrict = models.BooleanField(default=False)
    restrict_quantity = models.IntegerField(null=True, blank=True)


class ProductImage(BaseProductModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    product_images = models.ImageField(upload_to="products")