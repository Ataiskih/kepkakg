from django.contrib import admin
from .models import *


class OrderListInLine(admin.TabularInline):
    model = OrderList


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ["name", "phone_number", "email"]
    inlines = [OrderListInLine]


@admin.register(OrderList)
class OrderListAdmin(admin.ModelAdmin):
    list_display = ["id", "customer", "complete", "created"]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ["product", "order_list", "quantity"]


@admin.register(Shipping)
class ShippingAdmin(admin.ModelAdmin):
    list_display = ["customer", "order_list", "address", "note"]