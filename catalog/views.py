from rest_framework import viewsets

from .models import Brand, Category, ProductType
from .serializers import BrandSerializer, CategorySerializer, ProductTypeSerializer


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.filter(is_active=True).order_by("sort_order", "name")
    serializer_class = CategorySerializer
    lookup_field = "slug"
    search_fields = ("name", "description")
    ordering_fields = ("name", "sort_order", "created_at")


class BrandViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Brand.objects.filter(is_active=True).order_by("name")
    serializer_class = BrandSerializer
    lookup_field = "slug"
    search_fields = ("name", "description")
    ordering_fields = ("name", "created_at")


class ProductTypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ProductType.objects.filter(is_active=True).order_by("name")
    serializer_class = ProductTypeSerializer
    lookup_field = "slug"
    search_fields = ("name", "description")
    ordering_fields = ("name", "created_at")