from django.shortcuts import render
from projects.models import Project
from blog.models import Post


def index(request):
    context = {
        'projects': Project.objects.all(),
        'posts': Post.objects.all()[:4]
    }
    return render(request, 'pages/index.html', context)
