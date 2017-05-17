from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.article_list, name='article_list'),
    url(r'^article/(?P<pk>\d+)/$', views.article_detail, name='article_detail'),
    url(r'^article/new/$', views.article_new, name='article_new'),
    url(r'^article/(?P<pk>\d+)/edit/$', views.article_edit, name='article_edit'),    
    url(r'^article/(?P<pk>\d+)/remove/$', views.article_remove, name='article_remove'),
    url(r'^article/(?P<section>.+)/filter/$', views.article_section, name='article_filter'),
]
