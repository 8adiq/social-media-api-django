from .models import Comment,Like
from rest_framework import serializers



class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id','post','user','content','created_at']


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id','post','user']