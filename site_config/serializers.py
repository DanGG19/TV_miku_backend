from rest_framework import serializers

from .models import SiteConfiguration


class SiteConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteConfiguration
        fields = (
            "id",
            "business_name",
            "slogan",
            "logo",
            "favicon",
            "whatsapp_number",
            "whatsapp_default_message",
            "email",
            "phone",
            "address",
            "facebook_url",
            "instagram_url",
            "tiktok_url",
            "primary_color",
            "secondary_color",
            "button_color",
            "navbar_color",
            "footer_color",
            "show_prices",
            "show_stock",
            "show_brands",
            "show_featured_products",
            "show_whatsapp_button",
            "show_contact_info",
            "show_about_section",
            "show_banner",
            "created_at",
            "updated_at",
        )