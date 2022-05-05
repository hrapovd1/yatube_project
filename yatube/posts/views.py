from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import render
from typing import Any


def index(request: HttpRequest) -> HttpResponse:
    context = {
        'index': 'Это главная страница проекта Yatube',
    }
    template = 'posts/index.html'
    return render(request, template, context)


def group_posts(request: HttpRequest, slug: Any) -> HttpResponse:
    context = {
        'group_posts': 'Здесь будет информация о группах проекта Yatube',
        'slug': slug,
    }
    template = 'posts/group.html'
    return render(request, template, context)
