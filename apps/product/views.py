from rest_framework import generics, permissions
from .models import CategoryModel, ProductModel
from .serializers import CategorySerializers, ProductSerializers


class CategoryListCreate(generics.ListCreateAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializers
    permission_classes = [permissions.IsAdminUser]


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializers
    permission_classes = [permissions.IsAdminUser]


class ProductListCreate(generics.ListCreateAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializers
    permission_classes = [permissions.IsAdminUser]


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializers
    permission_classes = [permissions.IsAdminUser]

