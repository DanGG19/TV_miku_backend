from django.db import models

from core.models import TimeStampedModel


class HomeBanner(TimeStampedModel):
    title = models.CharField(max_length=180)
    subtitle = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to="banners/home/")
    cta_text = models.CharField(max_length=80, blank=True)
    cta_link = models.URLField(blank=True)
    is_active = models.BooleanField(default=True, db_index=True)
    sort_order = models.PositiveIntegerField(default=0, db_index=True)

    class Meta:
        ordering = ["sort_order", "id"]
        verbose_name = "Home Banner"
        verbose_name_plural = "Home Banners"
        indexes = [
            models.Index(fields=["is_active", "sort_order"]),
        ]

    def __str__(self):
        return self.title