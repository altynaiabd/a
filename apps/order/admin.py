from django.contrib import admin
from .models import OrderModel, OrderItemModel

# Register your models here.

@admin.register(OrderModel)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at', 'updated_at', 'order_sum',)
    search_fields = ('user_id__email',)

@admin.register(OrderItemModel)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'product_id', 'quantity',)
    search_fields = ('product_id__name',)