from rest_framework import viewsets
from .models import CategoryModel, ProductModel
from .serializers import CategorySerializers, ProductSerializers

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializers

class ProductViewSet(viewsets.ModelViewSet):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializers
