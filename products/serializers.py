from rest_framework import serializers

from .models import Product, ProductImage


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = (
            "id",
            "image",
            "alt_text",
            "sort_order",
            "created_at",
        )


class ProductListSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    brand = serializers.StringRelatedField()
    product_type = serializers.StringRelatedField()
    effective_availability = serializers.ReadOnlyField()

    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "slug",
            "short_description",
            "price",
            "compare_price",
            "stock",
            "is_available",
            "is_featured",
            "effective_availability",
            "category",
            "brand",
            "product_type",
            "main_image",
            "created_at",
            "updated_at",
        )


class ProductDetailSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    brand = serializers.StringRelatedField()
    product_type = serializers.StringRelatedField()
    images = ProductImageSerializer(many=True, read_only=True)
    effective_availability = serializers.ReadOnlyField()

    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "slug",
            "short_description",
            "description",
            "sku",
            "price",
            "compare_price",
            "stock",
            "is_available",
            "is_featured",
            "effective_availability",
            "category",
            "brand",
            "product_type",
            "main_image",
            "images",
            "created_at",
            "updated_at",
        )