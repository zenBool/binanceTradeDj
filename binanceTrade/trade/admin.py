from django.contrib import admin
from .models import Article


# Register your models here.


# @admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'type', 'created_at')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content', 'pub_date')


admin.site.register(Article, ArticleAdmin)
