from rest_framework.routers import DefaultRouter

from .views import HomeBannerViewSet

router = DefaultRouter()
router.register(r"banners", HomeBannerViewSet, basename="banner")

urlpatterns = router.urls