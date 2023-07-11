from rest_framework import generics
from .serializer import UserSerializer, FriendshipsSerializer, UserCoursesSerializer
from .models import User, UserCourse

# Create your views here.

class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class FriendshipsListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = FriendshipsSerializer

class UserFriendsDetailAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = FriendshipsSerializer

class UserLessonsListAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserCoursesSerializer


    