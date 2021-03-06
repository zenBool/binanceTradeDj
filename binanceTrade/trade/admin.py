from django.contrib import admin
from .models import Article, Category


# Register your models here.


# @admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created_at')
    list_display_links = ('id', 'title')
    list_editable = ('category',)
    list_filter = ('category', 'likes')
    search_fields = ('title', 'content', 'pub_date')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title', )


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
