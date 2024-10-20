from django.urls import path,include
from .views import CommentViewset,LikeViewset
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'comments', CommentViewset)
router.register(r'likes',LikeViewset)


urlpatterns = [
    path('',include(router.urls))
]