from django.contrib import admin
from .models import Category, Post

class CategoryAdmin(admin.ModelAdmin):
     readonly_fields = ('created_at', 'updated_at')

class PostAdmin(admin.ModelAdmin):
     readonly_fields = ('created_at', 'updated_at')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
