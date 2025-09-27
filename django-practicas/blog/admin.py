from django.contrib import admin
from .models import Post, Comment

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'autor')
    search_fields = ('title', 'autor')
    list_filter = ('created_at', 'autor')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'created_at')
    search_fields = ('author',)
    list_filter = ('created_at',)

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)