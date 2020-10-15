from django.contrib import admin
from product.models import (
    Product,
    ProductCharacteristic,
    ProductAdditionalImages,
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
