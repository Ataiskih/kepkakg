from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from product.views import *


urlpatterns = [
    path('all/', products, name='products'),
    path('<int:pk>/', product, name='product_detail'),
    path('category/<int:pk>/', category, name='category'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)