from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from product.views import ProductDetailView


urlpatterns = [
    path('<int:pk>/', ProductDetailView.as_view(), name='product'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, docoment_root=settings.MEDIA_ROOT)