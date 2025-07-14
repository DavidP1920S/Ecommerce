from django.urls import path
from Commerce.views import index, product_list_view

app_name = "Comercio"

urlpatterns = [
path("", index, name="index"),
path("products/", product_list_view, name="product-list")

]
