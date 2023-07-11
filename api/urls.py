from django.urls import path, include
from rest_framework import routers
from api import views


urlpatterns=[
    path('users/', views.UserListAPIView.as_view(), name='users-list'),
    path('friendships/', views.FriendshipsListAPIView.as_view(), name='friendship-list'),
    path('user/<int:pk>/friends/', views.UserFriendsDetailAPIView.as_view(), name='user-friends-list'),
    path('user/<int:pk>/lessons/', views.UserLessonsListAPIView.as_view(), name='user-lessons-list'),
]