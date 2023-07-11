from rest_framework import serializers
from .models import User, Course, UserCourse

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name']

class FriendshipsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class UserCourseSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True)

    class Meta:
        model = UserCourse
        fields = ['course', 'lessons_taken']

class UserCoursesSerializer(UserSerializer):
    """gets all courses for an specific user"""
    
    courses = serializers.SerializerMethodField('get_courses')
    
    def get_courses(self, obj):
        users = obj.usercourse_set.all().filter(lessons_taken__gt=0).prefetch_related('user')
        serializer = UserCourseSerializer(users, many=True)
        return serializer.data
    
    class Meta:
        model = User
        fields = ['name', 'courses']