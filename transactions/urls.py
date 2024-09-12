from django.urls import path
from . import views

urlpatterns = [
    path("", views.menu, name="menu"),
    path("add_to_cart/<uuid:product_id>", views.add_to_cart, name="add_to_cart"),
    path("cart", views.cart, name="cart"),
    path("success", views.success, name="success"),
    path("contact", views.contact, name="contact")
]
