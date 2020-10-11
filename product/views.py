from django.shortcuts import render
from django.http import Http404
from django.views.generic import (
    ListView,
    DetailView,
)
from product.models import(
    Product,
    ProductCharacteristic,
)


# main page (all products page)
class ProductListView(ListView):
    template_name = 'product/main.html'
    model = Product
    paginate_by = 50
    
    def get_context_data(self, **kwargs):
        try:
            context = super().get_context_data(**kwargs)
            context['product'] = Product.objects.filter(
                availability=True,
                deleted=False                
            )
        except context['product'].DoesNotExist:
            raise Http404("Ох, нет объекта")
        return context


# product page
class ProductDetailView(DetailView):
    template_name = 'product/product.html'
    model = Product
