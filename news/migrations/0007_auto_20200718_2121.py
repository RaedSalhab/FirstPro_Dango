# Generated by Django 3.0.7 on 2020-07-18 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_auto_20200718_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_class',
            field=models.CharField(default='Unclassified', max_length=100),
        ),
    ]
