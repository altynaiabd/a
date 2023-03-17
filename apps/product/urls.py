from django.urls import path
from . import views


urlpatterns = [
                    path('category/', views.CategoryListCreate.as_view()),
                    path('category-detail/', views.CategoryDetail.as_view()),

                    path('product-list/', views.ProductListCreate.as_view()),
                    path('product-detail/', views.ProductDetail.as_view()),
]
