from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from postapp.models import Post


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'content', 'author', 'image']


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

