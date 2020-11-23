from django.contrib import admin
from product.models import (
    Product,
    ProductCharacteristic,
    ProductAdditionalImages,
    Category
)


class ProductAdditionalImagesInline(admin.TabularInline):
    model = ProductAdditionalImages
    fields = ['addentional_images',]
    extra = 1


class ProductCharacteristicInline(admin.TabularInline):
    model = ProductCharacteristic
    fields = ['material', 'size', 'color']
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    exclude = ('updated',)
    inlines = [
        ProductAdditionalImagesInline,
        ProductCharacteristicInline
    ]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Category
    fields = ["name"]