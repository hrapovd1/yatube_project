from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import render
from typing import Any


def index(request: HttpRequest) -> HttpResponse:
    template = 'posts/index.html'
    return render(request, template)


def group_posts(request: HttpRequest, slug: Any) -> HttpResponse:
    return HttpResponse(f'А здесь посты из группы: {slug}')
