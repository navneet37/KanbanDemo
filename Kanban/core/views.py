from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserSerializer


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
