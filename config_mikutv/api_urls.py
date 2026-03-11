from django.urls import include, path

urlpatterns = [
    path("catalog/", include("catalog.urls")),
    path("products/", include("products.urls")),
    path("site/", include("site_config.urls")),
    path("cart/", include("cart.urls")),
    path("cms/", include("cms.urls")),
]