from django.db import models

from core.models import NamedBaseModel


class Category(NamedBaseModel):
    image = models.ImageField(upload_to="categories/", blank=True, null=True)
    sort_order = models.PositiveIntegerField(default=0, db_index=True)

    class Meta:
        ordering = ["sort_order", "name"]
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        indexes = [
            models.Index(fields=["is_active", "sort_order"]),
            models.Index(fields=["slug"]),
            models.Index(fields=["name"]),
        ]


class Brand(NamedBaseModel):
    logo = models.ImageField(upload_to="brands/", blank=True, null=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "Brand"
        verbose_name_plural = "Brands"
        indexes = [
            models.Index(fields=["is_active", "name"]),
            models.Index(fields=["slug"]),
        ]


class ProductType(NamedBaseModel):
    class Meta:
        ordering = ["name"]
        verbose_name = "Product Type"
        verbose_name_plural = "Product Types"
        indexes = [
            models.Index(fields=["is_active", "name"]),
            models.Index(fields=["slug"]),
        ]