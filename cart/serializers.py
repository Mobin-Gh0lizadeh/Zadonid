from rest_framework import serializers


class AddToCartSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    quantity = serializers.IntegerField()


class DeleteCartItemSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()