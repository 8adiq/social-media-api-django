from .models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email','bio','profile_picture','password']
        extra_kwargs = { 'password' : {'write_only': True}}

    def create(self,validated_data):
        user = User.objects.create(
            email = validated_data['email'],
            username = validated_data['username'],
            bio = validated_data.get('bio',''),
            profile_picture = validated_data.get('profile_picture',None),
        )
        user.set_password(validated_data['password'])
        user.save()
        return user