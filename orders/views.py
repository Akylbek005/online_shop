from rest_framework import generics
from rest_framework.response import Response

from products.serializer import ProductsSerializer
from users.serializers import UsersSerializer
from orders.serializers import OrdersSerializer

from products.models import Products
from users.models import User
from orders.models import Orders


class OrdersView(generics.GenericAPIView):
    """В разработке"""
    serializer_class = OrdersSerializer
    queryset = Orders.objects.all()

    def get(self, request):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)


class OrdersCreateView(generics.GenericAPIView):
    """В разработке"""
    serializer_class = OrdersSerializer
    queryset = Orders.objects.all()

    def post(self, request):
        data = request.data
        serializer_products = ProductsSerializer(data=data)
        serializer_user = UsersSerializer(data=data)
        if serializer_products.is_valid() and serializer_user.is_valid():
            serializer_user.validated_data()
            serializer_products.validated_data()

        return Response({'ok': '200'})

