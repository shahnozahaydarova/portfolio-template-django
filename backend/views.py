from django.shortcuts import render
from .models import *


def home(request):
    posts = Post.objects.all()
    context = {
        'posts':posts
    }
    return render(request,'index.html',context)

def homeslug(request,slug):
    post = Post.objects.get(slug=slug)
    context = {
        'post':post
    }
    return render(request,'post.html',context)