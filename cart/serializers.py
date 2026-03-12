from rest_framework import serializers


class CartItemInputSerializer(serializers.Serializer):
    product_id = serializers.IntegerField(min_value=1)
    quantity = serializers.IntegerField(min_value=1)


class CartValidateSerializer(serializers.Serializer):
    items = CartItemInputSerializer(many=True)

    def validate_items(self, value):
        if not value:
            raise serializers.ValidationError("You must send at least one item.")
        return value


class CartWhatsAppPreviewSerializer(serializers.Serializer):
    customer_name = serializers.CharField(max_length=120, required=False, allow_blank=True)
    customer_note = serializers.CharField(required=False, allow_blank=True)
    items = CartItemInputSerializer(many=True)

    def validate_items(self, value):
        if not value:
            raise serializers.ValidationError("You must send at least one item.")
        return value