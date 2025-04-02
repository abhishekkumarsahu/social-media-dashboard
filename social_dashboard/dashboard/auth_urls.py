from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import register, profile, fetch_twitter_posts, facebook,logout
from . import views

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='dashboard/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', profile, name='profile'),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('twitter/posts/', fetch_twitter_posts, name='twitter_posts'),
    path('facebook', views.facebook, name='facebook'),
]
