from django.urls import path
from postapp.api.views import (
    post_create_view,
    post_get_view,
    user_create_view,
    user_get_view,
)

app_name = "postapp"

urlpatterns = [
    path('post/<int:post_id>',  post_get_view,      name="GETPOST" ),
    path('post/create/',        post_create_view,   name="CREATEPOST"),

    path('user/<str:username>', user_get_view,      name="GETUSER"),
    path('user/create/',        user_create_view,   name="CREATEUSER"),
]