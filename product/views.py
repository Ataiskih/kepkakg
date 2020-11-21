from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import Http404

from product.models import Product, ProductCharacteristic, ProductAdditionalImages
from order.utils import cartData


def products(request):
    context = {}
    data = cartData(request)
    cartItems = data['cartItems']
    context['cartItems'] = cartItems

    object_list = Product.objects.filter(
        availability=True,
        deleted=False 
        )
    paginator = Paginator(object_list, 50)
    context['object_list'] = object_list

    return render(request, 'main.html', context)


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

    return render(request, 'product.html', context)


def info(request):
    return render(request, 'info.html')