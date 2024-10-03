from rest_framework import serializers
from django.contrib.auth import get_user_model


User = get_user_model() # get whatever user is in use
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id','first_name','last_name','username','bio','profile_picture']
