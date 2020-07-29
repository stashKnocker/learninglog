"""defining url for learning log."""
from django.urls import path
from . import views 

urlpatterns = [
     # Home page
    path('', views.index, name='index'),
    # Page that shows all topics.
    path('topics/', views.topics, name='topics'),
    # Detail page for a single topic.
    path('<int:topic_id>/topic/', views.topic, name='topic'),
    # Page for adding a new topic
    path('new_topic/', views.new_topic, name='new_topic'),
    # Page for adding a new entry
    path('<int:topic_id>/new_entry/', views.new_entry, name='new_entry'),
    # Page for editing an entry.
    path('<int:entry_id>/edit_entry/', views.edit_entry, name='edit_entry'),
]