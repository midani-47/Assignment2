from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime
from django.contrib import messages
from .models import Journey, Post
from .forms import PostForm, JourneyForm, CommentForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone


def post_list(request):
    # posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    posts =Post.objects.all().order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post= get_object_or_404(Post, pk=pk)
    comments= post.comments.filter(approved=True)
    new_comment= None
    if request.method =='POST':
        comment_form =CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment= comment_form.save(commit=False)
            new_comment.post= post
            new_comment.author=request.user
            new_comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        comment_form= CommentForm()
    is_author= post.author==request.user
    is_liked = post.likes.filter(id=request.user.id).exists() if request.user.is_authenticated else False
    return render(request, 'blog/post_details.html', {
        'post': post,
        'comments':comments,
        'new_comment':new_comment,
        'comment_form':comment_form,
        'is_author':is_author,
        'is_liked': is_liked
    })




def home(request):
    # my logic for displaying the homepage content (like the latest blog posts)
    context ={"sitetitle": "VanLife","slogan": "Hey vanlifers! Let's hit the road"}  # i will edit context data for the template spaettter
    return render(request, 'base_generic.html', context)


@login_required
def post_new(request):
    if request.method == "POST":
        form =PostForm(request.POST)
        if form.is_valid():
            post= form.save(commit=False)
            post.author= request.user
            post.save()
            messages.success(request, 'Your post has been created successfully!')
            return redirect('post_detail', pk=post.pk)
    else:
        form= PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})




@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.author != request.user:
        return redirect('post_detail', pk=pk)
    if request.method=="POST":
        post.delete()
        messages.success(request, 'Your post has been deleted suchestfully!')
        return redirect('post_list')
    return render(request, 'blog/post_confirm_delete.html', {'post': post})


@login_required
def post_edit(request, pk):
    post= get_object_or_404(Post, pk=pk)
    if post.author != request.user:
        messages.error(request, "what do you think you're doing? HUH? this ain't your post!")
        return redirect('post_detail', pk=pk)
    if request.method== "POST":
        form=PostForm(request.POST, instance=post)
        if form.is_valid():
            post= form.save(commit=False)
            post.author = request.user
            post.published_date= timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form= PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def blog_feed(request):
    query= request.GET.get('q')
    author= request.GET.get('author')
    date_from=request.GET.get('date_from')
    date_to=request.GET.get('date_to')
    post_list= Post.objects.all().order_by('-created_date')
    journey_list= Journey.objects.all().order_by('-start_date')
    if query:
        post_list= post_list.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        ).distinct()
        journey_list= journey_list.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        ).distinct()
    if author:
        post_list=post_list.filter(author__username__icontains=author)
    if date_from:
        post_list= post_list.filter(created_date__gte=datetime.strptime(date_from, '%Y-%m-%d'))

    if date_to:
        post_list= post_list.filter(created_date__lte=datetime.strptime(date_to, '%Y-%m-%d'))
    paginator= Paginator(post_list, 10)  # Show 10 posts per page
    page=request.GET.get('page')
    try:
        posts= paginator.page(page)
    except PageNotAnInteger:
        posts= paginator.page(1)
    except EmptyPage:
        posts= paginator.page(paginator.num_pages)
    return render(request, 'blog/blog_feed.html', {
        'posts': posts,
        'journeys': journey_list,
        'query':query,
        'author':author,
        'date_from': date_from,
        'date_to': date_to
    })




@login_required
def post_like(request, pk):
    post= get_object_or_404(Post, pk= pk)
    if request.user in post.likes.all():
        post.likes.remove(request.user)

    else:
        post.likes.add(request.user)
    return redirect('post_detail', pk=pk)


@login_required
def post_unlike(request, pk):
    post=get_object_or_404(Post, pk= pk)
    post.likes.remove(request.user)
    return redirect('post_detail', pk=pk)


@login_required
def journey_new(request):

    if request.method=="POST":
        form= JourneyForm(request.POST)
        if form.is_valid():
            journey= form.save(commit=False)
            journey.author = request.user
            journey.save()
            return redirect('journey_detail', pk=journey.pk)
    else:
        form= JourneyForm()
    return render(request, 'blog/journey_edit.html', {'form': form})


@login_required
def journey_list(request):
    journeys= Journey.objects.all()
    return render(request, 'blog/journey_list.html', {'journeys': journeys})


def journey_detail(request, pk):

    journey= get_object_or_404(Journey, pk=pk)
    is_participant= journey.participants.filter(id=request.user.id).exists() if request.user.is_authenticated else False
    participants= journey.participants.all()
    return render(request, 'blog/journey_detail.html', {
        'journey':journey,
        'is_participant': is_participant,
        'participants':participants
    })
@login_required
def journey_join(request, pk):
    journey= get_object_or_404(Journey, pk=pk)
    journey.participants.add(request.user)
    return redirect('journey_detail', pk=pk)

@login_required
def journey_leave(request, pk):

    journey=get_object_or_404(Journey, pk= pk)
    journey.participants.remove(request.user)
    return redirect('journey_detail', pk= pk)