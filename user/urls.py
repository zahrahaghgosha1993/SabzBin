from django.urls import path

from user import views

urlpatterns = [
    path('', views.UserListAPIView.as_view(), name='user_list'),
    ]