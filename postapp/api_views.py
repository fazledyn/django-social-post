from django.http import JsonResponse, HttpResponse, HttpResponseNotFound

from .serializers import PostSerializer
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

        return JsonResponse(postSerialized.data, safe=False)

