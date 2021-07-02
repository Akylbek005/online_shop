from rest_framework import serializers

from .models import Product, OrderModels


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderModels
        fields = '__all__'

