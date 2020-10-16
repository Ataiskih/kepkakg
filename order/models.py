from django.db import models
from django.contrib.auth.models import User

from product.models import BaseAbstractModel, Product


class Customer(BaseAbstractModel):
    user = models.OneToOneField(
        to=User,
        null=True, blank=True,
        on_delete=models.CASCADE,
    )
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=255)

    def __str__(self):
        return self.name


class OrderList(BaseAbstractModel):
    customer = models.ForeignKey(
        to=Customer,
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name="order_list"
    )
    complete = models.BooleanField(default=False)

    @property
    def get_cart_total(self):
        order_items = self.order_item.all()
        total = sum([item.get_item_total for item in order_items])
        return self.total


class OrderItem(BaseAbstractModel):
    product = models.ForeignKey(
        to=Product,
        on_delete=models.CASCADE,
        related_name="order_item"
    )
    order_list = models.ForeignKey(
        to=OrderList,
        on_delete=models.CASCADE,
        related_name="order_item"
    )
    quantity = models.IntegerField(default=1)

    @property
    def get_item_total(self):
        total = self.product.new_price * self.quantity
        return self.total


class Shipping(models.Model):
    customer = models.ForeignKey(
        to=Customer,
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name="shipping"
    )
    order_list = models.ForeignKey(
        to=OrderList,
        on_delete=models.CASCADE,
        related_name="shipping"
    )
    address = models.CharField(
        max_length=255,
        null=True, blank=True
    )
    note = models.CharField(
        max_length=255,
        null=True, blank=True
    )