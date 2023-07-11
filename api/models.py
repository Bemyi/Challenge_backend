from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    friends = models.ManyToManyField('self')
    
class Course(models.Model):
    name = models.CharField(max_length=100)

class UserCourse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    lessons_taken = models.IntegerField(default=0)