from django.db import models
from apps.abstractmodel import AbstractModel

# Create your models here.

    
class CategoryModel(AbstractModel):
    name = models.CharField(verbose_name='Категория', max_length=20)
    slug = models.SlugField(max_length=200, db_index=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self) -> str:
        return self.category

class ProductModel(AbstractModel):
    name = models.CharField(verbose_name='Наименование товара', max_length=50)
    category = models.ForeignKey(CategoryModel, verbose_name='Категория', max_length=30, related_name='products', on_delete=models.CASCADE)
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(verbose_name='Цена', max_digits=12, decimal_places=2)
    quantity = models.PositiveIntegerField(verbose_name='Количество')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self) -> str:
        return self.product_name
