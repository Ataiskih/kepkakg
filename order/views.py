from django.shortcuts import render
from django.http import JsonResponse
import json

from .models import *
from .utils import *


def cart(request):
	data = cartData(request)
	cartItems = data('cartItems')
	order_list = data('order_list')
	items = data('items')

	context = {'items':items, 'order_list':order_list, 'cartItems':cartItems}
	return render(request, 'order/cart.html', context)


def checkout(request):
	data = cartData(request)
	cartItems = data('cartItems')
	order_list = data('order_list')
	items = data('items')

	context = {'items':items, 'order_list':order_list, 'cartItems':cartItems}

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


def processOrder(request):
	data = json.loads(request.body) # checkout.html 114

	if request.user.is_authenticated:
		customer = request.user.customer
		order_list, created = OrderList.objects.get_or_create(customer=customer, complete=False)
	else:
		customer, order_list = guestOrder(request, data)

	total = float(data['form']['total']) # checkout.html 100 строка

	if total == order_list.get_cart_total:
		order_list.complete = True
	order_list.save()

	order_list.shipping = Shipping.objects.create(
		customer=customer,
		order_list=order_list,
		address=data['shipping']['address'],
		note=data['shipping']['note']
		)
else:
		

	return JsonResponse('Payment submitted..', safe=False)