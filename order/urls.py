from django.urls import path
from order.views import *

urlpatterns =  [
    path("cart/", cart, name="cart"),
    path("checkout/", checkout, name="checkout"),
    path("update_item/", updateItem, name="update_item"),
    path('/process_order/', processOrder, name="process_order"),
    path("info/", info, name="info"),
    path("order_list/", ordersList, name="orders_list"),
]