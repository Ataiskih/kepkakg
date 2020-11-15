from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from product.views import products, product

urlpatterns = [
    path('all/', products, name='products'),
    path('<int:pk>/', product, name='product_detail'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)