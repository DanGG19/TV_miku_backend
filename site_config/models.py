from django.core.validators import RegexValidator
from django.db import models

from core.models import TimeStampedModel


hex_color_validator = RegexValidator(
    regex=r"^#(?:[0-9a-fA-F]{3}|[0-9a-fA-F]{6})$",
    message="Enter a valid HEX color, for example #FFFFFF.",
)


class SiteConfiguration(TimeStampedModel):
    business_name = models.CharField(max_length=180)
    slogan = models.CharField(max_length=255, blank=True)

    logo = models.ImageField(upload_to="site/logo/", null=True, blank=True)
    favicon = models.ImageField(upload_to="site/favicon/", null=True, blank=True)

    whatsapp_number = models.CharField(max_length=30, blank=True)
    whatsapp_default_message = models.CharField(max_length=255, blank=True)

    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=30, blank=True)
    address = models.TextField(blank=True)

    facebook_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    tiktok_url = models.URLField(blank=True)

    primary_color = models.CharField(
        max_length=7,
        default="#000000",
        validators=[hex_color_validator],
    )
    secondary_color = models.CharField(
        max_length=7,
        default="#FFFFFF",
        validators=[hex_color_validator],
    )
    button_color = models.CharField(
        max_length=7,
        default="#000000",
        validators=[hex_color_validator],
    )
    navbar_color = models.CharField(
        max_length=7,
        default="#FFFFFF",
        validators=[hex_color_validator],
    )
    footer_color = models.CharField(
        max_length=7,
        default="#000000",
        validators=[hex_color_validator],
    )

    show_prices = models.BooleanField(default=True)
    show_stock = models.BooleanField(default=True)
    show_brands = models.BooleanField(default=True)
    show_featured_products = models.BooleanField(default=True)
    show_whatsapp_button = models.BooleanField(default=True)
    show_contact_info = models.BooleanField(default=True)
    show_about_section = models.BooleanField(default=True)
    show_banner = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Site Configuration"
        verbose_name_plural = "Site Configuration"

    def __str__(self):
        return self.business_name or "Site Configuration"