from django.contrib import admin
from blog.models import Category, Post


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    exclude = ['slug']
    list_display = ['title', 'slug']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'user']
