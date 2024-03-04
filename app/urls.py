from django.urls import path

from app.views import UserAPIView, UserCreateAPIView, PostAPIView, PostCreateAPIView, CommentAPIView, \
    CommentCreateAPIView, LikeAPIView, LikeCreateAPIView

urlpatterns = [
    path('get/api/v1/users/', UserAPIView.as_view(), name='user'),
    path('post/api/v1/users/', UserCreateAPIView.as_view(), name='user'),
    path('get/api/v1/post/', PostAPIView.as_view(), name='post'),
    path('post/api/v1/post/', PostCreateAPIView.as_view(), name='post'),
    path('get/api/v1/comment/', CommentAPIView.as_view(), name='comment'),
    path('post/api/v1/comment/', CommentCreateAPIView.as_view(), name='comment'),
    path('post/api/v1/like/', LikeAPIView.as_view(), name='like'),
    path('post/api/v1/like/', LikeCreateAPIView.as_view(), name='like'),

]