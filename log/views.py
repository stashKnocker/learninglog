from django.shortcuts import render, redirect #render returns the complete template view.
#redirect the page to topics after submitted form.  
from .models import Topic, Entry
from django.contrib.auth.decorators import login_required
from .forms import TopicForm, EntryForm
from django.http import Http404

# Create your views here.
def index(request):
    """contains info of index page."""
    return render(request, 'log/index.html')

@login_required
def topics(request):
    """contains info of topics page."""
    topics = Topic.objects.filter(owner=request.user).order_by('date')
    context = {'topics': topics}
    return render(request, 'log/topics.html', context)

@login_required
def topic(request, topic_id):
    """contains info of each topic with entries."""
    topic = Topic.objects.get(id=topic_id)
    "make sure current user belongs to logged in user."
    if topic.owner != request.user:
        raise Http404

    entries = topic.entry_set.order_by ('-date')
    context = {'topic':topic, 'entries':entries}
    return render(request, 'log/topic.html', context)

@login_required
def new_topic(request):
    """direct user inputted data or blank form."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = TopicForm()
    else:
        # POST data submitted; process data.
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('log:topics')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'log/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    """Add a new entry for a particular topic."""
    topic = Topic.objects.get(id=topic_id)
    "make sure current user belongs to logged in user."
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = EntryForm()
    else:
        # POST data submitted; process data.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('log:topic', topic_id=topic_id)

    # Display a blank or invalid form.
    context = {'topic': topic, 'form': form}
    return render(request, 'log/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """Edit an existing entry."""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    "make sure current user belongs to logged in user."
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = EntryForm(instance=entry)
    else:
        # POST data submitted; process data.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('log:topic', topic_id=topic.id)

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'log/edit_entry.html', context)


