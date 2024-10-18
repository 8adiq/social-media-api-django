from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from .serializer import CommentSerializer,LikeSerializer
from .models import Comment,Like
from rest_framework import generics

# Create your views here.


class CommentView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class LikeView(generics.CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)