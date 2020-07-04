from django.shortcuts import render
from .models import Article
# Create your views here.
def index(request): #Main page view
    list_obj = Article.objects.all().order_by('-id')[:5]
    context = {
        'list_obj': list_obj
    }
    return render(request, 'news/index.html', context)

def detail(request,article_id): #Articles view
    obj = Article.objects.get(id=article_id)
    context = {
        'article_title':obj.article_title,
        'article_text': obj.article_text,
        'pub_date':obj.pub_date,
    }
    return render(request, 'news/detail.html',context)