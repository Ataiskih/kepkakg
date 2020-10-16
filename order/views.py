from django.shortcuts import render
from .models import *


def cart(request):
    context = {}
    if request.user.is_authentiated:
        customer = request.user.customer
        order_list, created = OrderList.objects.get_or_create(customer=customer, complete=False)
        items = order_list.order_item.all()
    else:
        items = []
        order_list = {'get_cart_total':0}
    context["items"] = items
    context["order_list"] = order_list
    return render(request, "product/cart.html", context)