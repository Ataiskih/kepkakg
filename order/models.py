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
    customer = models.ForeignKeY(
        to=Customer,
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name="order_list"
    )
    complete = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)


class OrderItem(BaseAbstractModel):
    product = models.ForeignKey(
        to=Product,
        on_delete=models.SET_NULL,
        related_name="order_item"
    )
    order_list = models.ForeignKey(
        tp=OrderList,
        on_delete=models.SET_NULL,
        related_name="order_item"
    )
    quantity = models.IntegerField(default=1)


class Shipping(models.Model):
    customer = models.ForeignKeY(
        to=Customer,
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name="shipping"
    )
    order_list = models.ForeignKey(
        tp=OrderList,
        on_delete=models.SET_NULL,
        related_name="shipping"
    )
    address = models.CharField(max_length=255, null=True)
    note = models.CharField(max_length=255)

    def __str__(self):
        return self.address