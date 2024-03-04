from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from app.models import User, Post, Comment, Like
from app.serializer import UserSerializer, UserCreateSerializer, PostSerializer, CommentSerializer, LikeSerializer


class UserAPIView(APIView):
    def get(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class UserCreateAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostAPIView(APIView):
    def get(self, request):
        queryset = Post.objects.all()
        serializer = PostSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class PostCreateAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentAPIView(APIView):
    def get(self, request):
        queryset = Comment.objects.all()
        serializer = CommentSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class CommentCreateAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LikeAPIView(APIView):
    def get(self, request):
        queryset = Like.objects.all()
        serializer = LikeSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class LikeCreateAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = LikeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
