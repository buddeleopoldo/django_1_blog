from django.conf.urls import url
#from django.urls import path
from . import views

app_name = 'blogs'
urlpatterns = [
    # Index page
    url(r'^$', views.index, name='index'),

    # Posts list
    url(r'^posts/$', views.posts, name='posts'),

    # Individual post detail
    url(r'^posts/(?P<post_id>\d+)/$', views.post, name='post'),

    # Add a new post
    url(r'^new_post/$', views.new_post, name='new_post'),

    # Edit an post
    url(r'^edit_post/(?P<post_id>\d+)/$', views.edit_post, name='edit_post'),
]