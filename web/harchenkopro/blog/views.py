from django.shortcuts import render
from .models import Post


def index(request):
    context = {
        'posts': Post.objects.filter(publish=True)
    }
    return render(request, 'blog/index.html', context)


def post(request, post_id):
    context = {'post': Post.objects.get(pk=post_id)}
    return render(request, 'blog/post.html', context)
