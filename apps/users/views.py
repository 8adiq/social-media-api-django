from django.shortcuts import render
from rest_framework import viewsets,generics
from rest_framework.permissions import AllowAny
from .models import User
from .serializer import UserSerializer


# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRegistration(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
