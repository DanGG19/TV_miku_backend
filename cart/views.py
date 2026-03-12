from urllib.parse import quote

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from products.models import Product
from site_config.models import SiteConfiguration

from .serializers import CartValidateSerializer, CartWhatsAppPreviewSerializer


class CartValidateView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = CartValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        items = serializer.validated_data["items"]
        product_ids = [item["product_id"] for item in items]

        products = Product.objects.filter(id__in=product_ids).select_related(
            "category",
            "brand",
            "product_type",
        )
        products_map = {product.id: product for product in products}

        result = []
        errors = []

        for item in items:
            product_id = item["product_id"]
            quantity = item["quantity"]
            product = products_map.get(product_id)

            if not product:
                errors.append(
                    {
                        "product_id": product_id,
                        "error": "Product not found.",
                    }
                )
                continue

            if not product.is_available:
                errors.append(
                    {
                        "product_id": product_id,
                        "product_name": product.name,
                        "error": "Product is not available.",
                    }
                )
                continue

            if product.stock < quantity:
                errors.append(
                    {
                        "product_id": product_id,
                        "product_name": product.name,
                        "requested_quantity": quantity,
                        "available_stock": product.stock,
                        "error": "Insufficient stock.",
                    }
                )
                continue

            result.append(
                {
                    "product_id": product.id,
                    "name": product.name,
                    "slug": product.slug,
                    "quantity": quantity,
                    "unit_price": str(product.price),
                    "subtotal": str(product.price * quantity),
                }
            )

        return Response(
            {
                "valid": len(errors) == 0,
                "items": result,
                "errors": errors,
            },
            status=status.HTTP_200_OK,
        )


class CartWhatsAppPreviewView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = CartWhatsAppPreviewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        items = serializer.validated_data["items"]
        customer_name = serializer.validated_data.get("customer_name", "").strip()
        customer_note = serializer.validated_data.get("customer_note", "").strip()

        product_ids = [item["product_id"] for item in items]
        products = Product.objects.filter(id__in=product_ids)
        products_map = {product.id: product for product in products}

        lines = ["Hello, I want to request the following products:"]
        validated_items = []
        errors = []
        total = 0

        for item in items:
            product_id = item["product_id"]
            quantity = item["quantity"]
            product = products_map.get(product_id)

            if not product:
                errors.append(
                    {
                        "product_id": product_id,
                        "error": "Product not found.",
                    }
                )
                continue

            if not product.is_available:
                errors.append(
                    {
                        "product_id": product_id,
                        "product_name": product.name,
                        "error": "Product is not available.",
                    }
                )
                continue

            if product.stock < quantity:
                errors.append(
                    {
                        "product_id": product_id,
                        "product_name": product.name,
                        "requested_quantity": quantity,
                        "available_stock": product.stock,
                        "error": "Insufficient stock.",
                    }
                )
                continue

            subtotal = product.price * quantity
            total += subtotal

            validated_items.append(
                {
                    "product_id": product.id,
                    "name": product.name,
                    "quantity": quantity,
                    "unit_price": str(product.price),
                    "subtotal": str(subtotal),
                }
            )

            lines.append(
                f"- {product.name} | Qty: {quantity} | Unit: {product.price} | Subtotal: {subtotal}"
            )

        if customer_name:
            lines.append("")
            lines.append(f"Customer name: {customer_name}")

        if customer_note:
            lines.append(f"Note: {customer_note}")

        lines.append("")
        lines.append(f"Estimated total: {total}")

        message = "\n".join(lines)

        site_config = SiteConfiguration.objects.order_by("-updated_at").first()
        whatsapp_number = ""
        whatsapp_url = ""

        if site_config and site_config.whatsapp_number:
            whatsapp_number = site_config.whatsapp_number
            whatsapp_url = f"https://wa.me/{whatsapp_number}?text={quote(message)}"

        return Response(
            {
                "valid": len(errors) == 0,
                "items": validated_items,
                "errors": errors,
                "message": message,
                "whatsapp_number": whatsapp_number,
                "whatsapp_url": whatsapp_url,
            },
            status=status.HTTP_200_OK,
        )