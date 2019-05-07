from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Event(models.Model):
    title = models.CharField(max_length=100, null=True)
    description = models.TextField(max_length=1000, null=True)
    allDay = models.BooleanField(null=True)
    start = models.DateTimeField()
    end = models.DateTimeField()
    url = models.URLField(null=True)
    user = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)


class Task(models.Model):
    title = models.CharField(max_length=100, null=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True)
