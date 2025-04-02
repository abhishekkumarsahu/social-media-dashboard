from django.urls import path, include
from . import views
from .views import home, create_post, like_post, comment_post, analytics_view, fetch_twitter_posts, tweet_fetch

urlpatterns = [
    path('', views.home, name='home'),
    path('auth/', include('dashboard.auth_urls')),  # Authentication URLs
    path('create/', create_post, name='create_post'),
    path('like/<int:post_id>/', like_post, name='like_post'),
    path('comment/<int:post_id>/', comment_post, name='comment_post'),
    path('analytics/', analytics_view, name='analytics'),
    # path('twitter', views.twitter, name='twitter'),
    path('twitter/', views.fetch_twitter_posts, name='twitter'),
    path('fetch-tweets/', tweet_fetch, name='tweet_fetch'),
     
]
