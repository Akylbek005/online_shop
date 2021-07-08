from rest_framework import viewsets, views, generics
from rest_framework.response import Response
from .serializers import OrdersSerializer

from .models import Orders


class OrdersView(views.APIView):

    def get(self, request):
        queryset = Orders.objects.all()
        serializer = OrdersSerializer(queryset, many=True)
        return Response(serializer.data)
