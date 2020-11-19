from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
<<<<<<< HEAD
from product.views import (
    Search,
    category,
    ProductListView,
    ProductDetailView,
)
=======
>>>>>>> 0acf90fe9e4172b81f80a49288bd81733d6d1ebb

from product.views import products, product


urlpatterns = [
<<<<<<< HEAD
    path('all/', ProductListView.as_view(), name='product'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('feedback/', include("feedback.urls")),
    path("category/<int:pk>/", category, name="category"),
    path('search/', Search.as_view(), name='search_product'),

=======
    path('all/', products, name='products'),
    path('<int:pk>/', product, name='product_detail'),
>>>>>>> 0acf90fe9e4172b81f80a49288bd81733d6d1ebb
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)