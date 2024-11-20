from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from .permission import IsOwnerOrReadOnly
from .serializer import CommentSerializer,LikeSerializer
from .models import Comment,Like
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

# Create your views here.

class CommentViewset(viewsets.ModelViewSet):
    """A viewset for viewing, creating, and deleting comments."""

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated,IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=False,methods=['GET'],url_path='post/(?P<post_id>[^/.]+)')
    def comments_by_post(self,request,post_id=None):
        comments = Comment.objects.filter(post_id=post_id)
        serializer = self.get_serializer(comments,many=True)
        return Response(serializer.data)

class LikeViewset(viewsets.ModelViewSet):
    """A viewset for viewing and creating likes."""

    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=False,methods=['GET','POST'],url_path='post/(?P<post_id>[^/.]+)')
    def number_of_likes(self,request,post_id=None):
        Likes = Like.objects.filter(post_id=post_id).count()
        return Response({'post_id':post_id, 'number of like': Likes})