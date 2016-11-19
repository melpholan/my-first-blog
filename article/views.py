from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.

def post_list(request):
    return render(request,'article/post_list.html',{})

