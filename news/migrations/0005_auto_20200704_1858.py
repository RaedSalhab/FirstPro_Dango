# Generated by Django 3.0.7 on 2020-07-04 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_article_article_sources'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_sources',
            field=models.CharField(default='Resources', max_length=2000),
        ),
    ]
