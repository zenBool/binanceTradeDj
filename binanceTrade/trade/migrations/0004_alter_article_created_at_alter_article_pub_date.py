# Generated by Django 4.0.4 on 2022-06-13 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0003_article_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
