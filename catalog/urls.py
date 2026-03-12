from rest_framework.routers import DefaultRouter

from .views import BrandViewSet, CategoryViewSet, ProductTypeViewSet

router = DefaultRouter()
router.register(r"categories", CategoryViewSet, basename="category")
router.register(r"brands", BrandViewSet, basename="brand")
router.register(r"product-types", ProductTypeViewSet, basename="product-type")

urlpatterns = router.urls