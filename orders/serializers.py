from rest_framework import serializers
from orders.models import Orders
from products.serializer import ProductsSerializer
from users.serializers import UsersSerializer


class OrdersSerializer(serializers.ModelSerializer):
    user = UsersSerializer()
    products = ProductsSerializer()

    class Meta:
        model = Orders
        fields = "__all__"
