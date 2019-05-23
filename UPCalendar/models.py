import datetime
from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    workTime = models.IntegerField(null=True, default=2)
    sleepTime = models.DateTimeField(null=True, default=datetime.datetime(2017, 11, 28, 21, 00))
    wakeUpTime = models.DateTimeField(null=True, default=datetime.datetime(2017, 11, 28, 7, 00))
    workOnWeekends = models.BooleanField(default=True)


class Event(models.Model):
    title = models.CharField(max_length=100, null=True)
    description = models.TextField(max_length=1000, null=True)
    allDay = models.BooleanField(default=False)
    start = models.DateTimeField()
    end = models.DateTimeField()
    color = models.CharField(max_length=7, default="#7B7B7B")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    recurrent = models.BooleanField(default=False)
    rrule = models.CharField(max_length=200, null=True)


class Task(models.Model):
    title = models.CharField(max_length=100, null=True)
    start = models.DateTimeField(null=True)
    description = models.TextField(max_length=1000, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    color = models.CharField(max_length=7, default="#B71C1C")
