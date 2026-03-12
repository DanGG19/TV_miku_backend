from django.urls import path

from .views import CartValidateView, CartWhatsAppPreviewView

urlpatterns = [
    path("validate/", CartValidateView.as_view(), name="cart-validate"),
    path("whatsapp-preview/", CartWhatsAppPreviewView.as_view(), name="cart-whatsapp-preview"),
]