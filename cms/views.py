from rest_framework import viewsets

from .models import HomeBanner
from .serializers import HomeBannerSerializer


class HomeBannerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = HomeBanner.objects.filter(is_active=True).order_by("sort_order", "id")
    serializer_class = HomeBannerSerializer
    ordering_fields = ("sort_order", "created_at")
    search_fields = ("title", "subtitle", "cta_text")