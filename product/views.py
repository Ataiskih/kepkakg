from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import Http404

from product.models import Product, ProductCharacteristic, ProductAdditionalImages, Category
from order.utils import cartData
from product.filters import ProductFilter


def products(request):
    data = cartData(request)
    cartItems = data['cartItems']

    f = ProductFilter(request.GET, queryset=Product.objects.filter(
        availability=True,
        deleted=False 
        ))

    context = {'cartItems':cartItems, 'filter': f}
    paginator = Paginator(f, 50)

    return render(request, 'product/main.html', context)


def product(request, pk):
    context = {}
    data = cartData(request)
    cartItems = data['cartItems']
    context['cartItems'] = cartItems

    try:
        product = Product.objects.get(id=pk)
        context['add_images'] = ProductAdditionalImages.objects.filter(product=product)
        context['all_characteristic'] = ProductCharacteristic.objects.filter(product=product)
        context['product'] = product
    except:
        context['type'] = 'danger'
        context['message'] = 'Не найдено'
        return render(request, 'message.html', context)

    return render(request, 'product/product.html', context)


def category(request, pk):
    context = {}
    context['products'] = Product.objects.filter(
        category__id=pk,
        availability=True,
        deleted=False
        )
    context['category_pk'] = pk

    return render(request, "product/products.html", context)
