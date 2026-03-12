from django.urls import path

from .views import SiteConfigurationDetailView

urlpatterns = [
    path("", SiteConfigurationDetailView.as_view(), name="site-config-detail"),
]