from django.contrib import admin

from .models import Brand, Category, ProductType


@admin.action(description="Mark selected categories as active")
def mark_categories_active(modeladmin, request, queryset):
    queryset.update(is_active=True)


@admin.action(description="Mark selected categories as inactive")
def mark_categories_inactive(modeladmin, request, queryset):
    queryset.update(is_active=False)


@admin.action(description="Mark selected brands as active")
def mark_brands_active(modeladmin, request, queryset):
    queryset.update(is_active=True)


@admin.action(description="Mark selected brands as inactive")
def mark_brands_inactive(modeladmin, request, queryset):
    queryset.update(is_active=False)


@admin.action(description="Mark selected product types as active")
def mark_product_types_active(modeladmin, request, queryset):
    queryset.update(is_active=True)


@admin.action(description="Mark selected product types as inactive")
def mark_product_types_inactive(modeladmin, request, queryset):
    queryset.update(is_active=False)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "is_active", "sort_order", "created_at")
    list_filter = ("is_active", "created_at")
    search_fields = ("name", "slug", "description")
    prepopulated_fields = {"slug": ("name",)}
    ordering = ("sort_order", "name")
    actions = (mark_categories_active, mark_categories_inactive)


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "is_active", "created_at")
    list_filter = ("is_active", "created_at")
    search_fields = ("name", "slug", "description")
    prepopulated_fields = {"slug": ("name",)}
    ordering = ("name",)
    actions = (mark_brands_active, mark_brands_inactive)


@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "is_active", "created_at")
    list_filter = ("is_active", "created_at")
    search_fields = ("name", "slug", "description")
    prepopulated_fields = {"slug": ("name",)}
    ordering = ("name",)
    actions = (mark_product_types_active, mark_product_types_inactive)