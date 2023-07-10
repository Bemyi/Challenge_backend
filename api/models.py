from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    friends = models.ManyToManyField('self', symmetrical=False)

class Lesson(models.Model):
    topic = models.CharField(max_length=100)
    
class Course(models.Model):
    name = models.CharField(max_length=100)
    lessons = models.ManyToManyRel(Lesson, though='CourseLesson')

class CourseLesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

class UserLesson(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)