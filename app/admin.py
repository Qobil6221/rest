from django.contrib import admin

from app.models import User, Post, Comment, Like

admin.site.register([User, Post, Comment, Like])