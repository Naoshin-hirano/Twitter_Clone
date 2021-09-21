from django.urls import path
from twitterapp.api.views import (TweetListCreateAPIView, TweetDetailAPIView)

urlpatterns = [
    path('tweets/', TweetListCreateAPIView.as_view(), name="tweet-list"),
    path('tweets/<int:pk>', TweetDetailAPIView.as_view(), name="tweet-detail"),
]