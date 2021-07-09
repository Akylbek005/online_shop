from rest_framework import serializers
from orders.models import Orders
from products.serializer import ProductsSerializer
from users.serializers import UserSerializer


class OrdersSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    products = ProductsSerializer()

    class Meta:
        model = Orders
        fields = "__all__"
