from django.db import models

class AbstractModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(AbstractModel):
    username = models.CharField(max_length = 50)
    full_name = models.CharField(max_length = 50)
    email = models.EmailField(max_length = 50)
    bithday = models.DateTimeField()
    bio = models.TextField()

    def __str__(self):
        return self.username

class Post(AbstractModel):
    title = models.CharField(max_length=128)
    body = models.TextField()
    is_active = models.BooleanField(default=True)
    user_id = models.ForeignKey(User, models.CASCADE, related_name='posts')

    def __str__(self):
        return self.title


class Comment(AbstractModel):
    body = models.TextField()
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')


class Like(AbstractModel):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')