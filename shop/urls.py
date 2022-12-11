from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register('category', CategoryViewSet, basename="category")
router.register('product', ProductViewSet, basename="product")
router.register('like', VoteViewSet, basename="like")
router.register('comment', CommentViewSet, basename="comment")
router.register('save', SaveViewSet, basename="save")
router.register('share', ShareViewSet, basename="share")

urlpatterns = [
    path("", include(router.urls)),
]