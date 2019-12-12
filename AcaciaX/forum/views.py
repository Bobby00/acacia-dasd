from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .forms import NewTopicForm, PostForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Topic, Post

def home(request):
    return render(request, 'index.html')

def forum(request):
    categories = Category.objects.all()
    return render(request, 'forum.html', {'categories': categories})

def category_topics(request, pk):
	try:
		category = get_object_or_404(Category, pk=pk)
	except Category.DoesNotExist:
		raise Http404
	return render(request, 'forum-topics.html', {'category': category})

def topic_posts(request, pk, topic_pk):
    topic = get_object_or_404(Topic, category__pk=pk, pk=topic_pk)
    return render(request, 'topic_posts.html', {'topic': topic})

@login_required
def new_topic(request, pk):
    category = get_object_or_404(Category, pk=pk)
    user = User.objects.first()  # TODO: get the currently logged in user
    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.category = category
            topic.starter = request.user
            topic.save()
            post = Post.objects.create(
                message=form.cleaned_data.get('message'),
                topic=topic,
                created_by=request.user
            )
            return redirect('topic_posts', pk=pk, topic_pk=topic.pk)  # TODO: redirect to the created topic page
    else:
        form = NewTopicForm()
    return render(request, 'new_topic.html', {'category': category, 'form': form})


@login_required
def reply_topic(request, pk, topic_pk):
    topic = get_object_or_404(Topic, category__pk=pk, pk=topic_pk)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.topic = topic
            post.created_by = request.user
            post.save()
            return redirect('topic_posts', pk=pk, topic_pk=topic_pk)
    else:
        form = PostForm()
    return render(request, 'reply_topic.html', {'topic': topic, 'form': form})