from django.contrib import admin
from .models import Tag, Category, Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'create_time','modified_time', 'category','author']
admin.site.register(Tag)
admin.site.register(Category)

#也要把PostAdmin注册进来
admin.site.register(Post,PostAdmin)