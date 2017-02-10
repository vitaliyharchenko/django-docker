from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='blog'),
    url(r'^post/(?P<post_id>\d+)$', views.post, name='post'),
]
