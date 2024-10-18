from .models import Post
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['id','text','image','video','created_at']
        read_only_fields = ['id','created_at']

    def create(self,validated_data):
        return Post.objects.create(**validated_data)
