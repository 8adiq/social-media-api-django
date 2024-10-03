from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet,UserRegistration
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView


router = DefaultRouter()
router.register(r'users',UserViewSet)

urlpatterns = [
    # path('token/',TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', UserRegistration.as_view(),name='user-registration'),
    path('',include(router.urls))
]