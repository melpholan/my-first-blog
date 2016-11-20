from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse
from django.utils  import  timezone
from article.models import Article

# Create your views here.

def post_list(request):

    article = Article.objects.filter(article_published_date__lte=timezone.now()).order_by('article_title')
    return render(request,'article/post_list.html',{'article':article})

def post_detail(request,pk):
    post = get_object_or_404(Article,pk=pk)
    return render(request, 'article/post_detail.html',{'post':post})

