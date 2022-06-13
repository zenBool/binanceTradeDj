# Generated by Django 4.0.4 on 2022-06-13 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0004_alter_article_created_at_alter_article_pub_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-created_at', 'title'], 'verbose_name': 'Статья', 'verbose_name_plural': 'Статьи'},
        ),
        migrations.RemoveField(
            model_name='article',
            name='body',
        ),
        migrations.AddField(
            model_name='article',
            name='content',
            field=models.TextField(blank=True, verbose_name='Содержание'),
        ),
        migrations.AlterField(
            model_name='article',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Создано'),
        ),
        migrations.AlterField(
            model_name='article',
            name='likes',
            field=models.IntegerField(default=0, verbose_name='Нравится'),
        ),
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Опубликовано'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='article',
            name='type',
            field=models.IntegerField(blank=True, choices=[(1, 'Type 1'), (2, 'Type 2')], verbose_name='Категория Статьи'),
        ),
    ]
