from rest_framework import viewsets
from .models import OrderModel, OrderItemModel
from .serializers import OrderSerializers, OrderItemSerializers

class OrderViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = OrderModel.objects.all()
    serializer_class = OrderSerializers

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItemModel.objects.all()
    serializer_class = OrderItemSerializers
