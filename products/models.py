from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.text import slugify

from core.models import TimeStampedModel


class Product(TimeStampedModel):
    name = models.CharField(max_length=180, db_index=True)
    slug = models.SlugField(max_length=200, unique=True, db_index=True, blank=True)
    short_description = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)

    sku = models.CharField(max_length=80, unique=True, null=True, blank=True, db_index=True)

    price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        db_index=True,
    )
    compare_price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        null=True,
        blank=True,
        validators=[MinValueValidator(0)],
    )

    stock = models.PositiveIntegerField(default=0, db_index=True)
    is_available = models.BooleanField(default=True, db_index=True)
    is_featured = models.BooleanField(default=False, db_index=True)

    category = models.ForeignKey(
        "catalog.Category",
        on_delete=models.PROTECT,
        related_name="products",
    )
    brand = models.ForeignKey(
        "catalog.Brand",
        on_delete=models.PROTECT,
        related_name="products",
        null=True,
        blank=True,
    )
    product_type = models.ForeignKey(
        "catalog.ProductType",
        on_delete=models.PROTECT,
        related_name="products",
        null=True,
        blank=True,
    )

    main_image = models.ImageField(upload_to="products/main/", null=True, blank=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "Product"
        verbose_name_plural = "Products"
        indexes = [
            models.Index(fields=["name"]),
            models.Index(fields=["slug"]),
            models.Index(fields=["price"]),
            models.Index(fields=["stock"]),
            models.Index(fields=["is_available"]),
            models.Index(fields=["is_featured"]),
            models.Index(fields=["created_at"]),
            models.Index(fields=["category", "is_available"]),
            models.Index(fields=["brand", "is_available"]),
            models.Index(fields=["product_type", "is_available"]),
        ]
        constraints = [
            models.CheckConstraint(
                condition=models.Q(price__gte=0),
                name="product_price_gte_0",
            ),
            models.CheckConstraint(
                condition=models.Q(stock__gte=0),
                name="product_stock_gte_0",
            ),
        ]

    def __str__(self):
        return self.name

    @property
    def has_stock(self):
        return self.stock > 0

    @property
    def effective_availability(self):
        return self.is_available and self.stock > 0

    def clean(self):
        if self.compare_price is not None and self.compare_price < self.price:
            raise ValidationError(
                {"compare_price": "Compare price cannot be lower than price."}
            )

    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name)

        self.full_clean()
        super().save(*args, **kwargs)


class ProductImage(TimeStampedModel):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="images",
    )
    image = models.ImageField(upload_to="products/gallery/")
    alt_text = models.CharField(max_length=180, blank=True)
    sort_order = models.PositiveIntegerField(default=0, db_index=True)

    class Meta:
        ordering = ["sort_order", "id"]
        verbose_name = "Product Image"
        verbose_name_plural = "Product Images"
        indexes = [
            models.Index(fields=["product", "sort_order"]),
        ]

    def __str__(self):
        return f"{self.product.name} - Image {self.sort_order}"