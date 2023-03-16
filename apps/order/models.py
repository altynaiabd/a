from django.db import models
from apps.user.models import UserModel
from apps.product.models import ProductModel
from apps.abstractmodel import AbstractModel
# Create your models here.

class OrderModel(AbstractModel):
    user = models.ForeignKey(UserModel, verbose_name='Пользователь', related_name='orders', on_delete=models.CASCADE)
    order_sum = models.DecimalField( verbose_name='Сумма заказа', max_digits=12, decimal_places=2)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self) -> str:
        return self.id
    

class OrderItemModel(models.Model):
    order_id = models.ForeignKey(OrderModel, on_delete=models.CASCADE, related_name='order_item')
    product_id = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name='order_item')
    quantity = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'Товар в заказе'
        verbose_name_plural = 'Товары в заказах'