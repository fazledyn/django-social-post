from django.http import JsonResponse, HttpResponse, HttpResponseNotFound
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

from .serializers import PostSerializer, UserSerializer
from .views import create_post
from .models import Post


def createPost(request):
    if request.method == 'POST':
        print("Here !")
        create_post(request)
        return HttpResponse(status=200)
    
    else:
        return HttpResponseNotFound(status=404)


def getPost(request, id):
    if request.method == 'POST':
        return HttpResponseNotFound(status=404)

    else:
        post = Post.objects.get(pk=id)
        postSerialized = PostSerializer(post)

        if post is not None:
            return JsonResponse(postSerialized.data, safe=False)
        else:
            return HttpResponseNotFound

def getUser(request, name):
    if request.method == 'GET':
        user = User.objects.filter(username=name)
        serializedUser = UserSerializer(user[0])

        if user is not None:
            return JsonResponse(serializedUser.data, safe=False)
        else:
            return HttpResponseNotFound

    else:
        return HttpResponseNotFound

@csrf_exempt
def createUser(request):
    username = request.POST.get("username")
    password1 = request.POST.get("password1")
    password2 = request.POST.get("password2")

    new_user = User.objects.create_user(username=username, password=password1)
    new_user.save()
    print("new user creatd !")

    return HttpResponse(status=200)
