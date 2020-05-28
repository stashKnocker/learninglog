from django.shortcuts import render
from .models import Topic

# Create your views here.
def index(request):
    """contains info of index page."""
    return render(request, 'log/index.html')

def topics(request):
    """contains info of topics page."""
    topics = Topic.objects.order_by('date')
    context = {'topics': topics}
    return render(request, 'log/topics.html', context)

def topic(request, topic_id):
    """contains info of each topic with entries."""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by ('-date')
    context = {'topic':topic, 'entries':entries}
    return render(request, 'log/topic.html', context)

