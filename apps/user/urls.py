from django.urls import path, include
from .views import UserRegistration, UserDetail

urlpatterns = [
    path('user_list/', UserRegistration.as_view()),
    path('user_detail/', UserDetail.as_view()),
]