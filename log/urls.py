"""defining url for learning log."""
from django.urls import re_path
from . import views 

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^topics/$', views.topics, name='topics'),
    #url for single topic page.
    re_path(r'^topics/(?:topic-(?P<topic_id>\d+)/)?$', views.topic, name='topic'),

]