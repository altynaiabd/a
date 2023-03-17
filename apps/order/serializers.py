from rest_framework import serializers
from .models import *

class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = OrderModel
        fields = '__all__'


class OrderItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = OrderItemModel
        fields = '__all__'