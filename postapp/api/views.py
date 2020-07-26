from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import viewsets


from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from postapp.api.serializers import PostSerializer, UserSerializer
from postapp.models import Post
from postapp.models import Post

"""    Blog Post App
"""

class PostViewSet(viewsets.ViewSet):
    
    def list(self, request):
        queryset = Post.objects.all()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)
        

    def create(self, request):
        
        pass

    def retrieve(self, request):
        queryset = Post.objects.all()

    def update(self, request):
        pass

    def destroy(self, request):
        pass

