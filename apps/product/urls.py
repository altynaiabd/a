from django.urls import path
from . import views


urlpatterns = [
    path('category/', views.CategoryList.as_view()),
    path('category_detail/', views.CategoryDetail.as_view()),
    path('product_list/', views.ProductList.as_view()),
    path('product_detail/', views.ProductDetail.as_view()),
]
