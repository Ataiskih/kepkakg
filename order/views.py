from django.shortcuts import render
from django.http import JsonResponse
import json

from order.models import *
from order.utils import *
from product.models import Product


def cart(request):
	data = cartData(request)
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'cart.html', context)


def checkout(request):
	data = cartData(request)
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, "checkout.html", context)


def updateItem(request):
	data = json.loads(request.body)
	print(data)
	
	productId = data['productId']
	action = data['action']
	print('Action:', action)
	print('Product:', productId)


	customer = request.user.is_authenticated
	product = Product.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)
	print(created)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

		

	return JsonResponse('Item was added', safe=False)


def processOrder(request):
	data = json.loads(request.body) # checkout.html 114

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
	else:
		customer, order = guestOrder(request, data)

	total = (data['form']['total']) # checkout.html 100 строка

	if total == (order.get_cart_total):
		order.complete = True
	order.save()

	if order.shipping == True:
		Shipping.objects.create(
			customer=customer,
			order=order,
			address=data['shipping']['address']
			)

	return JsonResponse('Заказ выполнен', safe=False)


def info(request):
	data = cartData(request)
	cartItems = data['cartItems']
	context = {'cartItems':cartItems}

	return render(request, 'info.html', context)


def ordersList(request):
	data = cartData(request)
	cartItems = data['cartItems']
	
	if request.user.is_authenticated:
		customer = request.user.customer
		orders = Order.objects.filter(
			customer=customer,
			complete=True)

		context = {'cartItems':cartItems, 'orders': orders}
		return render(request, 'orders_list.html', context)
	else:
		context = {}
		context['type'] = 'danger'
		context['message'] = 'Пользователь не найден'
		return render(request, 'product/message.html', context)