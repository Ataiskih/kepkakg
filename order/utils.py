import json

from order.models import Customer, Order, OrderItem
from product.models import Product


def cookieCart(request):
    # создаем корзину для non-logged-in юзера
    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {}

    items = []
    order = {'get_cart_total':0, 'get_cart_items':0}
    cartItems = order['get_cart_items']

    for i in cart:
        try:
            cartItems += cart[i]['quantity'] # число товаров в корзине

            product = Product.objects.get(id=i)
            total = (product.old_price * cart[i]['quantity'])

            order['get_cart_total'] += total
            order['get_cart_total'] += cart[i]['quantity']

            item = {
				'id':product.id,
				'product':{'id':product.id,'name':product.name, 'price':product.old_price, 
				'image':product.main_image}, 'quantity':cart[i]['quantity'],
                }
            items.append(item)
        except:
            pass # если продукта по каким-то причинам нет в бд, ошибка выдаваться не будет
    
    return {'cartItems':cartItems, 'order':order, 'items':items}


def cartData(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
	else:
		cookieData = cookieCart(request)
		cartItems = cookieData['cartItems']
		order = cookieData['order']
		items = cookieData['items']

	return {'cartItems':cartItems, 'order':order, 'items':items}


def guestOrder(request, data): # для guests
	name = data['form']['name']
	email = data['form']['email']

	cookieData = cookieCart(request)
	items = cookieData['items']

	customer, created = Customer.objects.get_or_create(email=email)
	customer.name = name
	customer.save()

	order = Order.objects.create(
		customer=customer,
		complete=False,
		)

	for item in items:
		product = Product.objects.get(id=item['id'])
		orderItem = OrderItem.objects.create(
			product=product,
			order=order,
			quantity=item['quantity'],
		)
	return customer, order