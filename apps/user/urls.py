from django.urls import path, include
from .views import UserListCreate, UserDetail

urlpatterns = [
    path('user-list/', UserListCreate.as_view()),
    path('user-detail/', UserDetail.as_view()),
]