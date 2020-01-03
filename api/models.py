from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=64, blank=True, null=True)
    lastName = models.CharField(max_length=64, blank=True, null=True)
    groupName = models.CharField(max_length=64, blank=True, null=True)

    def __str__(self):
        return self.user.username


class TimerType(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Timer(models.Model):
    name = models.CharField(max_length=128)
    active = models.BooleanField(default=True)
    type = models.ForeignKey(TimerType, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    duration = models.FloatField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
