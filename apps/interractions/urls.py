from django.urls import path,include
from .views import CommentView,LikeView


urlpatterns = [
    path('comments/',CommentView.as_view(),name='comment-craete'),
    path('likes/',LikeView.as_view(),name='like-craete')
]