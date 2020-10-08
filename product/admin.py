from django.contrib import admin
from product.models import (
    Product,
    ProductCharacteristic,
)


@admin.register(Product)
class ProductAdminForm(admin.ModelAdmin):
    exclude = ('updated',)


@admin.register(ProductCharacteristic)
class ProductAdminForm(admin.ModelAdmin):
    exclude = ('product',)
