from rest_framework import serializers

from .models import HomeBanner


class HomeBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeBanner
        fields = (
            "id",
            "title",
            "subtitle",
            "image",
            "cta_text",
            "cta_link",
            "is_active",
            "sort_order",
            "created_at",
            "updated_at",
        )