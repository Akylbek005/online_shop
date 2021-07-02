from django.core.mail import send_mail
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView

from .serializer import ProductSerializer, OrderProductSerializer
from .models import Product, OrderProduct
from config.settings import EMAIL_HOST_USER


class AddProductView(GenericAPIView):
    serializer_class = ProductSerializer
    queryset = Product

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request):
        queryset = self.queryset.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class OrderProductView(GenericAPIView):
    serializer_class = OrderProductSerializer
    queryset = OrderProduct

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        data = serializer.data
        product = Product.objects.get(id=data.get('product'))
        send_mail('Online Shop', f'Здраствуйте {data.get("name")}.\n'
                                 f'Ваш заказ: Имя товара-{product.name}, цена-{product.price}\n',
                  EMAIL_HOST_USER, [data.get('email')])
        return Response(serializer.data, status=status.HTTP_201_CREATED)
