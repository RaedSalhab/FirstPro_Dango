import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Article(models.Model):
    article_title = models.CharField(max_length=100, default='SOME STRING')
    article_text = models.TextField()
    article_brief = models.CharField(max_length=200, default='brief')
    article_publisher = models.CharField(max_length=100, default='Name')
    article_class = models.CharField(max_length=100, default='Unclassified')
    pub_date = models.DateTimeField('date published')
    article_sources = models.CharField(max_length=2000, default='Sources')

    def __str__(self):
        return self.article_title
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

