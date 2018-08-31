from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import Article
# Create your views here.

def article_detail(request,article_id):
    try:
        wenzhang = Article.objects.get(id=article_id)
    except :
        raise Http404("文章不存在")
    
    return HttpResponse("文章标题:%s<br>文章内容:%s" % (wenzhang.title,wenzhang.content))
    