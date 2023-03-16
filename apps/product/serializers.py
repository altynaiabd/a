from rest_framework import serializers
from django_filters import rest_framework as filters
from .models import *

class CategoryFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = CategoryModel
        fields = ['name']

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = '__all__'

class ProductFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = filters.NumberFilter(field_name='price', lookup_expr='lte')
    category = filters.CharFilter(field_name='category__slug')

    class Meta:
        model = ProductModel
        fields = ['min_price', 'max_price', 'category']

class ProductSerializers(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField()
    category_slug = serializers.SerializerMethodField()

    class Meta:
        model = ProductModel
        fields = '__all__'

    def get_category_name(self, obj):
        return obj.category.name

    def get_category_slug(self, obj):
        return obj.category.slug


        
