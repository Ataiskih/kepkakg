from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import Http404
<<<<<<< HEAD
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
from product.forms import Category,CategoryCreateForm
from feedback.forms import FeedBackForm,FeedBack
# from .filters import ProductFilter


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


class Search(ListView):
    paginate_by = 3

    def get_queryset(self):
        return Product.objects.filter(
            description__icontains=self.request.GET.get('q'),
            vendor_code__icontains=self.request.GET.get('q'),
        )

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['q'] = f"q={self.request.GET.get('q')}"
        return render('index.html', context)



=======

from product.models import Product, ProductCharacteristic, ProductAdditionalImages
from order.utils import cartData


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
>>>>>>> 0acf90fe9e4172b81f80a49288bd81733d6d1ebb
