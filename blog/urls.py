from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.postList, name='postList'),
    url(r'^post/(?P<pk>\d+)/$', views.postDetail, name='postDetail'),
]