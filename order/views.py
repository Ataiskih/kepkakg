from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import *


def cart(request):
    context = {}
    if request.user.is_authentiated:
        customer = request.user.customer
        order_list, created = OrderList.objects.get_or_create(customer=customer, complete=False)
        items = order_list.order_item.all()
        items_count = order_list.get_items_count
    else:
        items = []
        order_list = {'get_cart_total':0, 'get_items_count':0}
        items_count = order_list["get_items_count"]

    context["items"] = items
    context["order_list"] = order_list
    context["items_count"] = items_count

    return render(request, "product/cart.html", context)


def checkout(request):
    context = {}
    if request.user.is_authentiated:
        customer = request.user.customer
        order_list, created = OrderList.objects.get_or_create(customer=customer, complete=False)
        items = order_list.order_item.all()
        items_count = order_list.get_items_count
    else:
        items = []
        order_list = {'get_cart_total':0, 'get_items_count':0}
        items_count = order_list["get_items_count"]

    context["items"] = items
    context["order_list"] = order_list

    return render(request, "product/checkout.html", context)


def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('Action:', action)
	print('Product:', productId)

	customer = request.user.customer
	product = Product.objects.get(id=productId)
	order_list, created = OrderList.objects.get_or_create(customer=customer, complete=False)

	order_item, created = OrderItem.objects.get_or_create(order_list=order_list, product=product)

	if action == 'add':
		order_item.quantity = (order_item.quantity + 1)
	elif action == 'remove':
		order_item.quantity = (order_item.quantity - 1)

	order_item.save()

	if order_item.quantity <= 0:
		order_item.delete()

	return JsonResponse('Item was added', safe=False)