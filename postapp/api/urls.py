from django.urls import path, include
from rest_framework import routers

from postapp.api.views import PostViewSet

app_name = "postapp"

router = routers.SimpleRouter(trailing_slash=True)
router.register(r'post', PostViewSet)

urlpatterns = router.urls