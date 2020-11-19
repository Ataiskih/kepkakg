from django import forms
from product.models import (
    Category,
    Product,
    ProductCharacteristic
)


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        exclude = [
            'new_price',
        ]


class CategoryCreateForm(forms.ModelForm):
     class Meta:
         model = Category
         fields = ['name']