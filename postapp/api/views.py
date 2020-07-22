from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.views import View

from postapp.api.serializers import PostSerializer, UserSerializer
from postapp.models import Post


"""    Blog Post App
"""

# CREATE
@api_view(['POST', ])
def post_create_view(request):

    if request.method == "POST":
        print(request.data)
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

# READ
@api_view(['GET',])
def post_get_view(request, post_id):

    if request.method == "GET":        
        post = Post.objects.get(pk=post_id)
        serializer = PostSerializer(post)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


""" User Account API
"""

@api_view(['GET', ])
def user_get_view(request, username):

    if request.method == "GET":
        user = User.objects.get(username=username)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST',])
def user_create_view(request):

    if request.method == "POST":
        username    = request.POST.get('username')
        password1   = request.POST.get('password1')
        password2   = request.POST.get('password2')
        user = User(username=username, password=password1)
        user.save()
        return Response(status=status.HTTP_201_CREATED)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
