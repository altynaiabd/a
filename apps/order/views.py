from rest_framework import generics, permissions
from .models import OrderModel, OrderItemModel
from .serializers import OrderSerializers, OrderItemSerializers


class OrderListCreate(generics.ListCreateAPIView):
    queryset = OrderModel.objects.all()
    serializer_class = OrderSerializers
    permission_classes = [permissions.IsAuthenticated]


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderModel.objects.all()
    serializer_class = OrderSerializers
    permission_classes = [permissions.IsAuthenticated]


class OrderItemListCreate(generics.ListCreateAPIView):
    queryset = OrderItemModel.objects.all()
    serializer_class = OrderItemSerializers
    permission_classes = [permissions.IsAuthenticated]


class OrderItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderItemModel.objects.all()
    serializer_class = OrderItemSerializers
    permission_classes = [permissions.IsAuthenticated]

