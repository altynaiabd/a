from django.urls import path
from . import views

urlpatterns = [
    path('order/', views.OrderList.as_view()),
    path('order_detail/', views.OrderDetail.as_view()),
    path('order_item_list/', views.OrderItemList.as_view()),
    path('order_item_detail', views.OrderItemDetail.as_view()),
]
