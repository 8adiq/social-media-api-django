from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import PostViewset
from .serializer import PostSerializer


router = DefaultRouter()
router.register(r'posts',PostViewset)

urlpatterns = [
    path('',include(router.urls))
]
