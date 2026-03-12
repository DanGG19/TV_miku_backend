from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from .filters import ProductFilter
from .models import Product
from .serializers import ProductDetailSerializer, ProductListSerializer


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = (
        Product.objects.select_related("category", "brand", "product_type")
        .prefetch_related("images")
        .order_by("-created_at")
    )
    filterset_class = ProductFilter
    search_fields = ("name", "short_description", "description", "sku")
    ordering_fields = ("price", "name", "created_at")
    lookup_field = "slug"

    def get_queryset(self):
        return self.queryset.filter(is_available=True)

    def get_serializer_class(self):
        if self.action == "retrieve":
            return ProductDetailSerializer
        return ProductListSerializer

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        return get_object_or_404(queryset, slug=self.kwargs["slug"])