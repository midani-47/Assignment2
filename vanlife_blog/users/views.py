from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
# from django.urls import reverse
from django.db.models import Q
from blog.models import Post, Journey
# from .models import Profile, CustomUser
# from ..blog.models import Post
from .forms import CustomUserCreationForm
# from .models import Profile


User= get_user_model()

def register(request):
    if request.method == 'POST':
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            username= form.cleaned_data.get('username')
            email=form.cleaned_data.get('email')

            if User.objects.filter(username= username).exists():
                messages.error(request, 'A user with that username already exists.')
            elif User.objects.filter(email= email).exists():
                messages.error(request, 'A user with that email already exists.')
            else:
                user = form.save()
                backend= 'django.contrib.auth.backends.ModelBackend'
                auth_login(request, user, backend= backend)
                return redirect("home")
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form=CustomUserCreationForm()
    return render(request, 'users/register.html', {'form':  form})

def home(request):
    return render(request,'user/home.html')

def login(request):
    if request.method == 'POST':
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user=form.get_user()
            auth_login(request, user)
            return redirect('home')
    else:
        form=AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

@login_required
def logout(request):
    return redirect('home')

# @login_required
def profile(request, username):
    profile_user= get_object_or_404(User, username=username)
    blogs=Post.objects.filter(author=profile_user)
    joined_journeys= Journey.objects.filter(participants=profile_user)
    liked_blogs= Post.objects.filter(likes=profile_user)

    print(f"Blogs for {profile_user.username}: {[blog.title for blog in blogs]}")

    return render(request, 'users/profile.html', {
        'profile_user':profile_user,
        'blogs': blogs ,
        'joined_journeys':joined_journeys,
        'liked_blogs': liked_blogs,
    })

def profile_blogs(request, username):
    profile_user= get_object_or_404(User, username=username)
    blogs= Post.objects.filter(author=profile_user)
    return render(request, 'users/profile_blogs.html', {
        'profile_user': profile_user,
        'blogs':blogs,
    })

def search(request):
    query= request.GET.get('q')
    if query:
        users = User.objects.filter(Q(username__icontains=query) | Q(profile__bio__icontains=query))
        posts= Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
        journeys = Journey.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
    else:
        users= User.objects.none()
        posts= Post.objects.none()
        journeys = Journey.objects.none()
    context={
        'users': users,
        'posts': posts,
        'journeys': journeys,
    }
    return render(request, 'users/search.html', context)




@login_required
def liked_blogs(request):
    liked_blogs = Post.objects.filter(likes=request.user)
    return render(request, 'users/liked_blogs.html', {'liked_blogs': liked_blogs})



