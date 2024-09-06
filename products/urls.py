
from django.urls import path
from . import views

urlpatterns = [
    path("product_form", views.product_form, name="product_form"),
    path("", views.index, name="index"),
    path("edit_product/<str:product_id>", views.edit_product, name="edit_product")
]
