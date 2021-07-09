from rest_framework import viewsets, views, generics
from rest_framework.response import Response
from .serializers import OrdersSerializer

from .models import Orders


class OrdersView(generics.GenericAPIView):
    serializer_class = OrdersSerializer
    queryset = Orders.objects.all()

    def get(self, request):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
