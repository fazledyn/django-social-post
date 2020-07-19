from django.urls import path
from . import api_views as views


urlpatterns = [
    path('create_post/',        views.createPost,   name='CreatePost'),
    path('get_post/<int:id>',   views.getPost,      name='GetPost'),
]