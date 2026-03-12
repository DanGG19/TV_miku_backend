from rest_framework import generics
from rest_framework.exceptions import NotFound

from .models import SiteConfiguration
from .serializers import SiteConfigurationSerializer


class SiteConfigurationDetailView(generics.RetrieveAPIView):
    serializer_class = SiteConfigurationSerializer

    def get_object(self):
        obj = SiteConfiguration.objects.order_by("-updated_at").first()
        if not obj:
            raise NotFound("Site configuration not found.")
        return obj