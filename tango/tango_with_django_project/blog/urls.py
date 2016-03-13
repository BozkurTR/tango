from django.conf.urls import patterns, url
from blog import views

urlpatterns = [
    url(r'^$',
        views.index,
        name='index'),
    url(r'^view/(?P<slug>[^\.]+).html',
        views.view_post,
        name='view_blog_post'),
    url(r'category/(?P<slug>[^\.]+).html',
        views.view_post,
        name='view_blog_category'),
]
