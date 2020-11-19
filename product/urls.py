from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from product.views import (
    Search,
    category,
    ProductListView,
    ProductDetailView,
)



urlpatterns = [
    path('all/', ProductListView.as_view(), name='product'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('feedback/', include("feedback.urls")),
    path("category/<int:pk>/", category, name="category"),
    path('search/', Search.as_view(), name='search_product'),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)