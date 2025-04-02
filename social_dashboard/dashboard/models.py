from django.db import models
from django.contrib.auth.models import User

# # Create your models here.

# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)  # Link to User model
#     bio = models.TextField(blank=True)
#     profile_picture = models.ImageField(upload_to="profile_pics/", blank=True)
#     twitter_handle = models.CharField(max_length=50, blank=True)
#     facebook_link = models.URLField(blank=True)

#     def __str__(self):
#         return self.user.username
    
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.user.username}: {self.content[:30]}"

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post')  # Ensure users can only like a post once

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}: {self.content[:30]}"

class Tweet(models.Model):
    tweet_id = models.CharField(max_length=250, null=True, blank=True)
    tweet_text = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.tweet_text