from django.contrib import admin
from .models import Post,Comment,Activities

admin.site.register(Post)

#comment system registeration

admin.site.register(Comment)

admin.site.register(Activities)


