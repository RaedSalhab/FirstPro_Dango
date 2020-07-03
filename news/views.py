from django.shortcuts import render
from .models import Article
# Create your views here.
def index(request):
    obj = Article.objects.get(id=6)
    context = {
        'article_title':obj.article_title,
        'article_text': obj.article_text,
        'pub_date':obj.pub_date,
    }
    return render(request, 'news/index.html', context)

def detail(request):
    return render(request, 'news/detail.html')