import django.utils.timezone
from django.db import models


# Create your models here.
class Article(models.Model):
    ARTICLE_TYPES = (
        (1, 'Type 1'),
        (2, 'Type 2'),
    )

    title = models.CharField(max_length=50)
    body = models.TextField()
    likes = models.IntegerField()
    type = models.IntegerField(choices=ARTICLE_TYPES)
    pub_date = models.DateTimeField(auto_now_add=True)
