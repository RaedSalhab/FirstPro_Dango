from django.db import models

# Create your models here.
class Article(models.Model):
    article_text = models.CharField(max_length=2000)
    pub_date = models.DateTimeField('date published')