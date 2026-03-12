from django.contrib import admin

from .models import Product, ProductImage


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    fields = ("image", "alt_text", "sort_order")
    ordering = ("sort_order", "id")


@admin.action(description="Mark selected products as available")
def mark_products_available(modeladmin, request, queryset):
    queryset.update(is_available=True)


@admin.action(description="Mark selected products as unavailable")
def mark_products_unavailable(modeladmin, request, queryset):
    queryset.update(is_available=False)


@admin.action(description="Mark selected products as featured")
def mark_products_featured(modeladmin, request, queryset):
    queryset.update(is_featured=True)


@admin.action(description="Unmark selected products as featured")
def unmark_products_featured(modeladmin, request, queryset):
    queryset.update(is_featured=False)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "sku",
        "price",
        "stock",
        "is_available",
        "is_featured",
        "category",
        "brand",
        "product_type",
        "created_at",
    )
    list_filter = (
        "is_available",
        "is_featured",
        "category",
        "brand",
        "product_type",
        "created_at",
    )
    search_fields = (
        "name",
        "slug",
        "sku",
        "short_description",
        "description",
    )
    prepopulated_fields = {"slug": ("name",)}
    ordering = ("name",)
    inlines = [ProductImageInline]
    actions = (
        mark_products_available,
        mark_products_unavailable,
        mark_products_featured,
        unmark_products_featured,
    )
    fieldsets = (
        (
            "Información general",
            {
                "fields": (
                    "name",
                    "slug",
                    "sku",
                    "short_description",
                    "description",
                )
            },
        ),
        (
            "Precio e inventario",
            {
                "fields": (
                    "price",
                    "compare_price",
                    "stock",
                    "is_available",
                    "is_featured",
                )
            },
        ),
        (
            "Clasificación",
            {
                "fields": (
                    "category",
                    "brand",
                    "product_type",
                )
            },
        ),
        (
            "Media",
            {
                "fields": ("main_image",),
            },
        ),
    )


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ("product", "sort_order", "created_at")
    list_filter = ("product", "created_at")
    search_fields = ("product__name", "alt_text")
    ordering = ("product", "sort_order", "id")