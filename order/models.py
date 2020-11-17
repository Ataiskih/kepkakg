from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

from product.models import Product


class Customer(models.Model):
    user = models.OneToOneField(
        to=User, null=True,
        blank=True,
        on_delete=models.CASCADE
        )
    name = models.CharField(max_length=255, null=True)
    phone_number = models.CharField(max_length=30)
    email = models.EmailField(max_length=255)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(
        to=Customer,
        null=True, blank=True,
        on_delete=models.SET_NULL
        )
    complete = models.BooleanField(default=False)
    order_date = models.DateTimeField(auto_now_add=True)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total
    
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


class OrderItem(models.Model):
    product = models.ForeignKey(
        to=Product,
        null=True,
        on_delete=models.SET_NULL,
        )
    order = models.ForeignKey(
        to=Order,
        null=True,
        on_delete=models.SET_NULL,
        )
    quantity = models.IntegerField(default=0)

    @property
    def get_total(self):
        total = self.product.old_price * self.quantity
        return total


class Shipping(models.Model):
    customer = models.ForeignKey(
        to=Customer,
        null=True, blank=True,
        on_delete=models.SET_NULL
        )
    order = models.ForeignKey(
        to=Order,
        null=True,
        on_delete = models.SET_NULL
        )
    address = models.CharField(max_length=255, null=True)
    note = models.CharField(
        max_length=255,
        null=True, blank=True
    )


def create_customer(sender, instance, created, **kwargs):
    if created:
        Customer.objects.create(user=instance)
        print("customer created")

post_save.connect(create_customer, sender=User)


def update_customer(sender, instance, created, **kwargs):
    if created == False:
        instance.customer.save()
        print("customer updated")

post_save.connect(update_customer, sender=User)