from django.shortcuts import render
from rest_framework import generics

from . import models
from . import serializers


class UserRegisterAPIView(generics.CreateAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserRegisterSerializer


