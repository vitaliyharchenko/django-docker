from django.conf.urls import url

from . import views

urlpatterns = [
    url('^$', views.projects_view, name='projects'),
    url('^(?P<project_id>\d+)$', views.project_view, name='project'),
]