from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.postList, name='postList'),
    url(r'^post/(?P<pk>\d+)/$', views.postDetail, name='postDetail'),
    url(r'^post/new/$', views.postNew, name='postNew'),
    url(r'^post/(?P<pk>\d+)edit/$', views.postEdit, name='postEdit'),
]