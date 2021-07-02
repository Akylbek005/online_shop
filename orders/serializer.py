from rest_framework import serializers

from .models import Product


class ProductSerializers(serializers.Serializer):

    class Meta:
        model = Product
        field = 'all'

