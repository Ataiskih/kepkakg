# import django_filters
# from django_filters import CharFilter
# from .models import Product

# class ProductFilter(django_filters.FilterSet):

#     description = CharFilter(field_name='description', lookup_expr='icontains'),
#     vendor_code = CharFilter(field_name='vendor_code', lookup_expr='icontains'),
#     categoty__name = CharFilter(field_name='categoty__name', lookup_expr='icontains')


#     class Meta:
#         model = Product
#         fields = ['vendor_code', 'description','category']