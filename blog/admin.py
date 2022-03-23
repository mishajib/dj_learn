from django.contrib import admin
from blog.models import Category, Post


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    exclude = ('slug',)
    list_display = ('title', 'slug',)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'user',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
