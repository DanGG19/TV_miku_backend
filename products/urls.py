from django.urls import path

from .views import ProductViewSet

product_list = ProductViewSet.as_view({"get": "list"})
product_detail = ProductViewSet.as_view({"get": "retrieve"})

urlpatterns = [
    path("", product_list, name="product-list"),
    path("<slug:slug>/", product_detail, name="product-detail"),
]