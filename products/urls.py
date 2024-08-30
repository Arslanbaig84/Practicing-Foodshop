
from django.urls import path
from . import views

urlpatterns = [
    path("product_form", views.product_form, name="product_form"),
    path("", views.index, name="index")
]
