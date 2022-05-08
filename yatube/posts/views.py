from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from typing import Any
from .models import Post
from .models import Group


def index(request: HttpRequest) -> HttpResponse:
    posts = Post.objects.order_by('-pub_date')[:5]
    context = {
        'posts': posts
    }
    template = 'posts/index.html'
    return render(request, template, context)


def group_posts(request: HttpRequest, slug: Any) -> HttpResponse:
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'group': group,
        'posts': posts,
    }
    template = 'posts/group_list.html'
    return render(request, template, context)
