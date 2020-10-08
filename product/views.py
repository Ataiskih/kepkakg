from django.shortcuts import render
from django.views.generic import DetailView
from product.models import(
    Product,
)
    

class ProductDetailView(DetailView):
    template_name = 'product/product.html'
    model = Product

    def get_context_data(self, **kwargs):
        pk = self.kwargs["pk"]
        product = Product.objects.get(id=pk)
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['product'] = Product.objects.get(id=pk)
        return context
