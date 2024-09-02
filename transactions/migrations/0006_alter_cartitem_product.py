# Generated by Django 4.2.5 on 2024-09-02 06:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_created_by_and_more'),
        ('transactions', '0005_alter_cartitem_order_quantity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_item', to='products.product'),
        ),
    ]
