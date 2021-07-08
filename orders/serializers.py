from rest_framework import serializers
from .models import Orders
from products.serializer import ProductsSerializer
from users.serializers import UserSerializer


class OrdersSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    products = ProductsSerializer(many=True)

    class Meta:
        model = Orders
        fields = "__all__"
