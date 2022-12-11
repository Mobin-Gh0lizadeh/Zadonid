from rest_framework import serializers
from .models import Order,OrderItem

class OrderSerializer(serializers.Serializer):
    address = serializers.CharField(max_length=500)