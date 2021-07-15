from rest_framework import viewsets
from rest_framework import permissions
from .serializer import ProductsSerializer
from .models import Products


class ProductView(viewsets.ModelViewSet):
    serializer_class = ProductsSerializer
    queryset = Products.objects.all()
    permission_classes = [permissions.IsAuthenticated]
