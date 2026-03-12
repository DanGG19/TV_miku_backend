import django_filters

from .models import Product


class ProductFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(field_name="category__slug")
    brand = django_filters.CharFilter(field_name="brand__slug")
    product_type = django_filters.CharFilter(field_name="product_type__slug")
    min_price = django_filters.NumberFilter(field_name="price", lookup_expr="gte")
    max_price = django_filters.NumberFilter(field_name="price", lookup_expr="lte")
    available = django_filters.BooleanFilter(method="filter_available")
    featured = django_filters.BooleanFilter(field_name="is_featured")

    class Meta:
        model = Product
        fields = [
            "category",
            "brand",
            "product_type",
            "min_price",
            "max_price",
            "available",
            "featured",
        ]

    def filter_available(self, queryset, name, value):
        if value is True:
            return queryset.filter(is_available=True, stock__gt=0)
        if value is False:
            return queryset.filter(stock=0) | queryset.filter(is_available=False)
        return queryset