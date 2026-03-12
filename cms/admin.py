from django.contrib import admin

from .models import HomeBanner


@admin.action(description="Mark selected banners as active")
def mark_banners_active(modeladmin, request, queryset):
    queryset.update(is_active=True)


@admin.action(description="Mark selected banners as inactive")
def mark_banners_inactive(modeladmin, request, queryset):
    queryset.update(is_active=False)


@admin.register(HomeBanner)
class HomeBannerAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active", "sort_order", "created_at")
    list_filter = ("is_active", "created_at")
    search_fields = ("title", "subtitle", "cta_text")
    ordering = ("sort_order", "id")
    actions = (mark_banners_active, mark_banners_inactive)