from tokenize import Comment
from rest_framework.serializers import ModelSerializer

from app.models import Like, Post, User, Comment

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UserCreateSerializer(ModelSerializer):
    def create(self, validated_data):
        username = validated_data['username']
        full_name = validated_data['full_name']
        email = validated_data['email']
        birthday = validated_data['birthday']
        bio = validated_data['bio']
        user = User(username=username, full_name=full_name, email=email, birthday=birthday, bio=bio)
        user.save()
        return user


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'body', 'is_active', 'user_id')


class PostCreateSerializer(ModelSerializer):
    def create(self, validated_data):
        title = validated_data['title']
        body = validated_data['body']
        is_active = validated_data['is_active']
        user_id = validated_data['user_id']
        post = Post(title=title, body=body, is_active=is_active, user_id=user_id)
        post.save()
        return post


class CommentSerializer(ModelSerializer):
    model = Comment
    fields = ('body', 'is_active', 'user_id', 'created_at')


class CommentCreateSerializer(ModelSerializer):
    def create(self, validated_data):
        body = validated_data['body']
        post_id = validated_data['post_id']
        user_id = validated_data['user_id']
        comment = Comment(body=body, post_id=post_id, user_id=user_id)
        comment.save()
        return comment


class LikeSerializer(ModelSerializer):
    model = Like
    fields = ('is_active', 'user_id', 'created_at')


class LikeCreateSerializer(ModelSerializer):
    def create(self, validated_data):
        post_id = validated_data['post_id']
        user_id = validated_data['user_id']
        like = Like(post_id=post_id, user_id=user_id)
        like.save()
        return like
    