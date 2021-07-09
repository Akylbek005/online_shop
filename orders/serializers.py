from rest_framework import serializers
from .models import Orders
from products.serializer import ProductsSerializer
from users.serializers import UserSerializer


class OrdersSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    products = ProductsSerializer(many=True, read_only=True)

    class Meta:
        model = Orders
        fields = "__all__"
