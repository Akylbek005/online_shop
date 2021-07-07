from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView

from .serializer import ProductSerializer
from .models import Product


class AddProductView(GenericAPIView):
    serializer_class = ProductSerializer
    queryset = Product

    def post(self, request):
        """ Отправьте сюда POST запрос что бы добавить продукт"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request):
        """ Отправьте сюда GET запрос что бы получить все продукты"""
        queryset = self.queryset.objects.filter(available=True)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
