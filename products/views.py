from django.shortcuts import render, HttpResponseRedirect
from products.models import ProductCategory, Product, Basket
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


def index(request):
    context = {
        "title": "Store",
        "discount": True
    }
    return render(request, "products/index.html", context)


def products(request, category_id=None, page_number=1):

    if category_id:
        products = Product.objects.filter(category=category_id)
    else:
        products = Product.objects.all()


    paginator = Paginator(products, per_page=3)
    products_paginator = paginator.page(page_number)

    context = {
        "title": "Store Products",
        "categories": ProductCategory.objects.all(),
        "products": products_paginator
        }

    return render(request, "products/products.html", context)


# basket add functionality ONLY!!!
@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)
    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
    
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


# basket delete functionality ONLY!!!
@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])