from email.mime import base
from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import PostViewSet, UserViewSet


router = SimpleRouter()
router.register("users", UserViewSet, basename="users")
router.register("", PostViewSet, basename="posts")

urlpatterns = router.urls
