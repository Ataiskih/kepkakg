from django.contrib import admin
from .models import *


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ["user", "name", "phone_number", "email"]


@admin.register(OrderList)
class OrderListAdmin(admin.ModelAdmin):
    list_display = ["id", "customer", "complete", "created"]
    inlines = [OrderItemInline]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ["product", "order_list", "quantity"]


@admin.register(Shipping)
class ShippingAdmin(admin.ModelAdmin):
    list_display = ["customer", "order_list", "address", "note"]