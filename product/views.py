from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import Http404
from django.views.generic import (
    ListView,
    DetailView,
)
from product.models import(
    Product,
    ProductCharacteristic,
    ProductAdditionalImages,
)
from django.views.generic.base import View
from product.forms import Category
from feedback.forms import FeedBackForm
from .filters import ProductFilter
from product.models import Product, ProductCharacteristic, ProductAdditionalImages
from order.utils import cartData


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
            context['filter'] = ProductFilter(self.request.GET,queryset=self.get_queryset())
        except context['product'].DoesNotExist:
            raise Http404("Ох, нет объекта")
        return context


# product page
class ProductDetailView(DetailView):
    template_name = 'product/product.html'
    model = Product

    def get_context_data(self, **kwargs):
        pk = self.kwargs["pk"]
        product = Product.objects.get(pk=pk)
        context = super().get_context_data(**kwargs)
        context['product'] = Product.objects.get(pk=pk)
        context['add_images'] = ProductAdditionalImages.objects.filter(
            product=product
        )
        context['all_characteristic'] = ProductCharacteristic.objects.filter(
            product=product
        )
        return context

def category(request, pk):
    context = {}
    context["category_pk"] = pk
    return render(request, "index.html", context)



def products(request):
    context = {}
    data = cartData(request)
    cartItems = data['cartItems']
    context['cartItems'] = cartItems

    object_list = Product.objects.filter(
        availability=True,
        deleted=False 
    )

    paginator = Paginator(object_list, 50)
    context['object_list'] = object_list

    return render(request, 'product/main.html', context)


def product(request, pk):
    context = {}
    data = cartData(request)
    cartItems = data['cartItems']
    context['cartItems'] = cartItems

    try:
        product = Product.objects.get(id=pk)
        context['add_images'] = ProductAdditionalImages.objects.filter(product=product)
        context['all_characteristic'] = ProductCharacteristic.objects.filter(product=product)
        context['product'] = product
    except:
        context['type'] = 'danger'
        context['message'] = 'Не найдено'
        return render(request, 'product/message.html', context)
    

    return render(request, 'product/product.html', context)




# class ProductListView(ListView):
#     template_name = 'product/main.html'
#     model = Product
#     paginate_by = 50
    
#     def get_context_data(self, **kwargs):
#         try:
#             context = super().get_context_data(**kwargs)
#             context['product'] = Product.objects.filter(
#                 availability=True,
#                 deleted=False                
#             )
#         except context['product'].DoesNotExist:
#             raise Http404("Ох, нет объекта")
#         return context


# class ProductDetailView(DetailView):
    # template_name = 'product/product.html'
    # model = Product

    # def get_context_data(self, **kwargs):
    #     pk = self.kwargs["pk"]
    #     product = Product.objects.get(pk=pk)
    #     context = super().get_context_data(**kwargs)
    #     context['product'] = Product.objects.get(pk=pk)
    #     context['add_images'] = ProductAdditionalImages.objects.filter(
    #         product=product
    #     )
    #     context['all_characteristic'] = ProductCharacteristic.objects.filter(
    #         product=product
    #     )
    #     return context
