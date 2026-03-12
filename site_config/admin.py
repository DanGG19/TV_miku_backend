from django.contrib import admin

from .models import SiteConfiguration


@admin.register(SiteConfiguration)
class SiteConfigurationAdmin(admin.ModelAdmin):
    list_display = (
        "business_name",
        "email",
        "phone",
        "show_prices",
        "show_stock",
        "show_whatsapp_button",
        "updated_at",
    )
    search_fields = (
        "business_name",
        "email",
        "phone",
        "whatsapp_number",
    )
    fieldsets = (
        (
            "Información del negocio",
            {
                "fields": (
                    "business_name",
                    "slogan",
                    "address",
                )
            },
        ),
        (
            "Branding",
            {
                "fields": (
                    "logo",
                    "favicon",
                    "primary_color",
                    "secondary_color",
                    "button_color",
                    "navbar_color",
                    "footer_color",
                )
            },
        ),
        (
            "Contacto",
            {
                "fields": (
                    "whatsapp_number",
                    "whatsapp_default_message",
                    "email",
                    "phone",
                )
            },
        ),
        (
            "Redes sociales",
            {
                "fields": (
                    "facebook_url",
                    "instagram_url",
                    "tiktok_url",
                )
            },
        ),
        (
            "Visibilidad del sitio",
            {
                "fields": (
                    "show_prices",
                    "show_stock",
                    "show_brands",
                    "show_featured_products",
                    "show_whatsapp_button",
                    "show_contact_info",
                    "show_about_section",
                    "show_banner",
                )
            },
        ),
    )

    def has_add_permission(self, request):
        if SiteConfiguration.objects.exists():
            return False
        return super().has_add_permission(request)