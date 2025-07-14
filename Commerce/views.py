from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Count

from Commerce.models import Product, Category, CartOrderItems,CartOrder, vendor, ProductsImages, ProductReview, Wishlist, Address


def index(request):
    #product = Product.objects.all()
    products = Product.objects.filter(product_status ="published",featured=True)


    context = {
        "products":products
    }
    return render(request, 'Commerce/index.html', context)

def product_list_view(request):
    products = Product.objects.filter(product_status ="published")


    context = {
        "products":products
    }


    return render(request, 'Commerce/product-list.html', context)
