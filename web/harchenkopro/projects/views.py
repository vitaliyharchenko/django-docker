from django.shortcuts import render
from .models import Project


# Create your views here.
def projects_view(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects.html', context)


def project_view(request, project_id):
    project = Project.objects.get(pk=project_id)
    project.views += 1
    project.save()
    context = {'project': project}
    return render(request, 'project.html', context)