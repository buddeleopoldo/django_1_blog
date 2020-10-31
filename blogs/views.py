from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404

from .models import BlogPost
from .forms import PostForm

def index(request):
    """ Index page """
    return render(request, 'blogs/index.html')

def posts(request):
    """ Posts list """
    posts = BlogPost.objects.order_by('date_added')
    context = {'posts': posts}
    return render(request, 'blogs/posts.html', context)

def post(request, post_id):
    """ Show a particular post detail """
    post = BlogPost.objects.get(id=post_id)
    description = post.text
    context = {'post': post, 'description': description}
    return render(request, 'blogs/post.html', context)

@login_required
def new_post(request):
    """ Add a new post"""
    if request.method != 'POST':
        # No data submitted, create blank form
        form = PostForm()
    else:
        # POST data submitted, process data
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.owner = request.user
            form.save()
            return HttpResponseRedirect(reverse('blogs:posts'))

    context = {'form': form}
    return render(request, 'blogs/new_post.html', context)

@login_required
def edit_post(request, post_id):
    """Edit an existing post."""
    post = BlogPost.objects.get(id=post_id)
    title = post.title
    text = post.text
    check_post_owner(request, post)

    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = PostForm(instance=post)
    else:
        # POST data submitted; process data.
        form = PostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blogs:post', args=[post.id]))

    context = {'post': post, 'title': title, 'text': text, 'form': form}
    return render(request, 'blogs/edit_post.html', context)

def check_post_owner(request, post):
    if post.owner != request.user:
        raise Http404