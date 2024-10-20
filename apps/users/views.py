from django.shortcuts import render
from .models import User
from .serializer import UserSerializer
from rest_framework import generics,viewsets
from rest_framework.permissions import AllowAny
# Create your views here.


class UserRegistration(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]