from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializer import ProductSerializer
from .models import Product


class AddProductAPIView(APIView):
    serializers = ProductSerializer
    queryset = Product

    def post(self, request):
        serializer = self.serializers(request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request, *args, **kwargs):
        queryset = self.queryset.objects.all()
        serializer = self.serializers(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


