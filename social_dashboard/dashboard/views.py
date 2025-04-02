from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Post, Like, Comment, Tweet
from .forms import PostForm, CommentForm
from django.http import JsonResponse
from social_django.models import UserSocialAuth
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Count
from .twitter import save_to_db
import requests


def home(request):
    # return HttpResponse("Welcome to the Social Media Dashboard!")
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'dashboard/home.html', {'posts': posts})

User = get_user_model()

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Explicitly set the backend
            user.backend = "django.contrib.auth.backends.ModelBackend"
            login(request, user, backend="django.contrib.auth.backends.ModelBackend")
            return redirect("/dashboard")   # Redirect to dashboard
    else:
        form = UserCreationForm()

    return render(request, "dashboard/register.html", {"form": form})


@login_required
def profile(request):
    return render(request, 'dashboard/profile.html')

@login_required(login_url='/login')
def logoutt(request):
    logout(request)
    return redirect('/login')

# @login_required
# def facebook(request):
#     api_url = "https://graph.facebook.com/v22.0/me?fields=id%2Cname&access_token=""
#     post = requests.get(api_url)
#     return render(request, 'dashboard/facebook.html', {'post': 'post'})

@login_required
def facebook(request):
    api_url = "https://graph.facebook.com/v22.0/me?fields=id%2Cname&access_token=YOUR_ACCESS_TOKEN"
    
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        data = response.json()  # Parse JSON response

        # Check if 'posts' key exists and has content
        if 'posts' in data and 'data' in data['posts']:
            posts = data['posts']['data']
        else:
            posts = []  # No posts available

    except requests.exceptions.RequestException as e:
        print("An error occurred while making the request:", e)
        posts = []  # No posts available in the event of an error

    return render(request, 'dashboard/facebook.html', {'posts': posts})

@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'dashboard/create_post.html', {'form': form})

@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    like, created = Like.objects.get_or_create(user=request.user, post=post)
    if not created:  # If already liked, remove like
        like.delete()
    return redirect('home')

@login_required
def comment_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return redirect('home')
    else:
        form = CommentForm()
    return render(request, 'dashboard/comment_post.html', {'form': form, 'post': post})

@login_required
def analytics_view(request):
    total_posts = Post.objects.count()
    total_likes = Like.objects.count()
    total_comments = Comment.objects.count()

    # Get top users by post count
    top_users = Post.objects.values('user__username').annotate(post_count=Count('id')).order_by('-post_count')[:5]

    # Recent Activity (Last 5 interactions)
    recent_posts = Post.objects.order_by('-created_at')[:5]
    recent_likes = Like.objects.order_by('-created_at')[:5]
    recent_comments = Comment.objects.order_by('-created_at')[:5]

    context = {
        'total_posts': total_posts,
        'total_likes': total_likes,
        'total_comments': total_comments,
        'top_users': top_users,
        'recent_posts': recent_posts,
        'recent_likes': recent_likes,
        'recent_comments': recent_comments,
    }
    return render(request, 'dashboard/analytics.html', context)

@login_required
def fetch_twitter_posts(request):
    tweets = Tweet.objects.order_by('-published_date')
    return render(request, 'dashboard/twitter.html', {'tweets': tweets})

@login_required
def tweet_fetch(request):
    save_to_db()
    return redirect('tweet_list')