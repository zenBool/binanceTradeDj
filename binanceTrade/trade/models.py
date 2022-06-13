import django.utils.timezone
from django.db import models


# Create your models here.
class Article(models.Model):
    ARTICLE_TYPES = (
        (1, 'Type 1'),
        (2, 'Type 2'),
    )

    title = models.CharField(max_length=50, verbose_name='Заголовок')
    content = models.TextField(blank=True, verbose_name='Содержание')
    likes = models.IntegerField(default=0, verbose_name='Нравится')
    type = models.IntegerField(choices=ARTICLE_TYPES, verbose_name='Категория Статьи', blank=True)
    pub_date = models.DateTimeField(auto_now=True, verbose_name='Опубликовано')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')

    def __str__(self):
        return f'Article {self.title}. Created at {self.created_at}'

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-created_at', 'title']
