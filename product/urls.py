from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    category,
    ProductListView,
    ProductDetailView,
    products,
    product,
)



urlpatterns = [
    path('all/', ProductListView.as_view(), name='product'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('feedback/', include("feedback.urls")),
    path("category/<int:pk>/", category, name="category"),

    path('all/', products, name='products'),
    path('<int:pk>/', product, name='product_detail'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)