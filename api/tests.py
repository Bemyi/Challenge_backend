from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import User, Course, UserCourse
from .serializer import UserSerializer, FriendshipsSerializer, UserCoursesSerializer

class UserListAPITest(APITestCase):
    def setUp(self):
        self.url = reverse('users-list')
        self.user1 = User.objects.create(name='Maria')
        self.user2 = User.objects.create(name='Luna')

    def test_list_users(self):
        """Check code 200 of the request and that the returned data is the same as the serialized data"""
        response = self.client.get(self.url)
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_list_users_invalid_method(self):
        """Check for invalid method"""
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

class FriendshipsListAPITest(APITestCase):
    def setUp(self):
        self.url = reverse('friendship-list')
        self.user1 = User.objects.create(name='Maria')
        self.user2 = User.objects.create(name='Luna')
        self.user3 = User.objects.create(name='Jorge')
        self.user1.friends.add(self.user2)
        self.user1.friends.add(self.user3)

    def test_list_friendships(self):
        """Check code 200 of the request and that the returned data is the same as the serialized data"""
        response = self.client.get(self.url)
        users = User.objects.all()
        serializer = FriendshipsSerializer(users, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_list_friendships_invalid_method(self):
        """Check for invalid method"""
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

class UserFriendsDetailAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create(name='Maria')
        self.friend1 = User.objects.create(name='Luna')
        self.friend2 = User.objects.create(name='Jorge')
        self.user.friends.add(self.friend1)
        self.user.friends.add(self.friend2)
        self.url = reverse('user-friends-list', kwargs={'pk': self.user.pk})

    def test_get_user_friends(self):
        """Check code 200 of the request and that the returned data is the same as the serialized data"""
        response = self.client.get(self.url)
        serializer = FriendshipsSerializer(self.user)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_user_friends_invalid_method(self):
        """Check for invalid method"""
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

class UserLessonsListAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create(name='Maria')
        self.course1 = Course.objects.create(name='Matematica')
        self.course2 = Course.objects.create(name='Español')
        self.user_course1 = UserCourse.objects.create(user=self.user, course=self.course1, lessons_taken=3)
        self.user_course2 = UserCourse.objects.create(user=self.user, course=self.course2, lessons_taken=5)
        self.url = reverse('user-lessons-list', kwargs={'pk': self.user.pk})

    def test_get_user_lessons(self):
        """Check code 200 of the request and that the returned data is the same as the serialized data"""
        response = self.client.get(self.url)
        serializer = UserCoursesSerializer(self.user)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_user_lessons_invalid_method(self):
        """Check for invalid method"""
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

class WeatherAPITest(APITestCase):
    def test_get_weather(self):
        """Check code 200 of the request and that the returned data is not None"""
        url = reverse('weather-api')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(response.data)