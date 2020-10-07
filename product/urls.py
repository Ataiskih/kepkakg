from django.urls import path
from product.views import product
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', product, name='product'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, docoment_root=settings.MEDIA_ROOT)