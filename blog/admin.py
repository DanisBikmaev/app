from django.contrib import admin
from .models import Post

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'published_date', 'status')
    list_filter = ('status', 'created_date', 'published_date', 'author')
    search_fields = ('title', 'body')
    raw_id_fields = ('author',)
    date_hierarchy = 'published_date'
    ordering = ['status', 'published_date']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)
