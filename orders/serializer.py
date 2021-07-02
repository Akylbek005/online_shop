from rest_framework import serializers

from .models import Product


<<<<<<< HEAD
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
=======
class ProductSerializers(serializers.Serializer):

    class Meta:
        model = Product
        field = 'all'

>>>>>>> db132f59df7cba061961621f8796fc12538a99e2
