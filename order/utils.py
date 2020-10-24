import json
from .models import *


def cookieCart(request):
    # создаем корзину для non-logged-in юзера
    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {}
    items = []
    order_list = {'get_cart_total':0, 'get_items_count':0}
    cartItems = order_list['get_items_count']

    for i in cart:
        try:
            cartItems += cart[i]['quantity'] # число товаров в корзине

            product = Product.objects.get(id=i)
            total = (product.price * cart[i]['quantity'])

            order_list['get_cart_total'] += total
            order_list['get_cart_total'] += cart[i]['quantity']

            item = {
                    'id':product.id,
                    'product':{'id':product.id,'name':product.name, 'price':product.new_price, 
                    'image':product.main_image}, 'quantity':cart[i]['quantity'],
                    }
            items.append(item)
        
        except:
            pass # если продукта по каким-то причинам нет в бд, ошибка выдаваться не будет
    
    return {'cartItems':cartItems, 'order_list':order_list, 'items':items}


def cartData(request):
    if request.user.is_authenticated:
		customer = request.user.customer
		order_list, created = OrderList.objects.get_or_create(customer=customer, complete=False)
		items = order_list.order_item.all()
		cartItems = order_list.get_items_count
	else:
		cookieData = cookieCart(request)
		cartItems = cookieData('cartItems')
		order_list = cookieData('order_list')
		items = cookieData('items')

        return {'cartItems':cartItems, 'order_list':order_list, 'items':items}