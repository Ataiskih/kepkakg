from django import forms
from product.models import (
    Product,
    ProductCharacteristic
)


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        exclude = [
            'new_price',
        ]