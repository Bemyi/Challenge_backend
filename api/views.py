from rest_framework import generics
from .serializer import UserSerializer, FriendshipsSerializer, UserCoursesSerializer, WeatherSerializer
from .models import User
import urllib.request
from django.http import JsonResponse
import json

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

class WeatherAPIView(generics.ListAPIView):
    serializer_class = WeatherSerializer

    def get_queryset(self):
        url = f"https://api.open-meteo.com/v1/forecast?latitude=-34.9215&longitude=-57.9545&daily=temperature_2m_max,temperature_2m_min&timezone=auto&forecast_days=1"

        try:
            with urllib.request.urlopen(url) as response:
                data = response.read().decode('utf-8')
                parsed_data = json.loads(data)
                return [parsed_data]

        except urllib.error.URLError as e:
            error_message = str(e.reason)
            return JsonResponse({'error': error_message})
    