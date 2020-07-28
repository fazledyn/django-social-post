from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status, viewsets

from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from postapp.api.serializers import PostSerializer, UserSerializer
from postapp.models import Post

"""    Blog Post App
"""

class PostViewSet(viewsets.ModelViewSet):
    
    queryset = Post.objects.all()
    serializer_class = PostSerializer