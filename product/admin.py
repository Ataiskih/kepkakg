from django.contrib import admin
from product.forms import Category
from product.models import (
    Product,
    ProductCharacteristic,
    ProductAdditionalImages,
    Category
)


class ProductAdditionalImagesAdminInline(admin.TabularInline):
    model = ProductAdditionalImages
    fields = ['addentional_images',]
    extra = 1


class ProductCharacteristicAdminInline(admin.TabularInline):
    model = ProductCharacteristic
    fields = ['material', 'size', 'color']
    extra = 0


@admin.register(Product)
class ProductAdminForm(admin.ModelAdmin):
    exclude = ('updated',)
    inlines = [
        ProductAdditionalImagesAdminInline,
        ProductCharacteristicAdminInline,
    ]

@admin.register(Category)
class Category(admin.ModelAdmin):
    model = Category
    fields = ["name"]