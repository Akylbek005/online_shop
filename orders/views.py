from django.core.mail import send_mail
from django.shortcuts import render
from rest_framework import status, viewsets, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView

from .serializer import ProductSerializer, OrdersSerializer
from .models import Product, OrderModels
from config.settings import EMAIL_HOST_USER

class AddProductAPIView(GenericAPIView):
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


class OrderSafeAndSendEmailViewSet(generics.GenericAPIView):
    serializer_class = OrdersSerializer
    queryset = OrderModels.objects.all()

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        send_mail('Новый заказ', f'Пользователь {data["first_name"]} заказал {data["product"]}.\n'
                  f'Его данные: номер телефона-{data["phone"]}',
                  EMAIL_HOST_USER, ['jumagylov1@gmail.com',])
        return Response(serializer.data, status=status.HTTP_201_CREATED)



