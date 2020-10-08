from django.shortcuts import render
from django.views.generic import ListView
from product.models import(
    Product,
)
    

class ProductListView(ListView):
    template_name = 'product/main.html'
    model = Product
    paginate_by = 50
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = Product.objects.filter(
            availability=True,
            deleted=False                
        )
        return context
