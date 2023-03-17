from django.urls import path
from . import views

urlpatterns = [
    path('order-list/', views.OrderListCreate.as_view()),
    path('order-detail/', views.OrderDetail.as_view()),
    path('order-item-list/', views.OrderItemListCreate.as_view()),
    path('order-item-detail', views.OrderItemDetail.as_view()),
]
