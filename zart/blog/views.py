from django.http import HttpResponse
from django.shortcuts import render
from .models import post

def index(request):
    mypost = post.objects.all()
    return render(request, 'blog/index.html',{'mypost': mypost})


def about(request):
    return HttpResponse("hello about")


def contact(request):
    return HttpResponse("hello contact")


def postView(request, pid):
    posts=post.objects.filter(id= pid) [0]
    return render(request, 'blog/blogPost.html', {'posts': posts})
