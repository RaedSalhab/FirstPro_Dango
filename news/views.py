from django.shortcuts import render
from .models import Article
# Create your views here.
def index(request):
    return render(request, 'news/index.html')

def detail(request):
    return render(request, 'news/detail.html')