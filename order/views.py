from django.shortcuts import render
from django.http import JsonResponse
import json

from order.models import *
from order.utils import cartData, guestOrder
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
	productId = data['productId']
	action = data['action']
	print('Action:', action)
	print('Product:', productId)

	customer = request.user.customer
	product = Product.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)

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

	total = float(data['form']['total']) # checkout.html 100 строка

	if total == float(order.get_cart_total):
		order.complete = True
	order.save()

	if order.shipping:
		Shipping.objects.create(
			customer=customer,
			order=order,
			address=data['shipping']['address']
			)

	return JsonResponse('Заказ выполнен', safe=False)


def info(request):
    return render(request, 'info.html')


def ordersList(request, id):
	data = cartData(request)
	cartItems = data['cartItems']
	orders_db = Order.objects.all()
	customer = Customer.objects.get(id=id)
	orders = customer.customer_orders # 2 3 4
	print(orders) # <QuerySet [<Order: Order object (2)>, <Order: Order object (3)>, <Order: Order object (4)>]>
	print([order.order_date for order in orders]) # [datetime.datetime(2020, 11, 22, 12, 19, 43, 357439, tzinfo=<UTC>), datetime.datetime(2020, 11, 22, 22, 43, 39, 734938, tzinfo=<UTC>), datetime.datetime(2020, 11, 22, 22, 43, 43, 688649, tzinfo=<UTC>)]
	context = {'cartItems':cartItems, 'orders': orders}
	return render(request, 'orders_list.html', context)