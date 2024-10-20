from django.shortcuts import render
from rest_framework import viewsets,generics
from .permissions import IsOwnerOrReadOnly
from .models import Post
from .serializer import PostSerializer
from rest_framework.permissions import IsAuthenticated


# Create your views here.

class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated,IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(username=self.request.user)





