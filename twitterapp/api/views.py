from rest_framework import generics
from twitterapp.models import post
from twitterapp.api.serializers import PostSerializer


class TweetListCreateAPIView(generics.ListCreateAPIView):
    queryset = post.objects.all().order_by("-id")
    serializer_class = PostSerializer


class TweetDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = post.objects.all()
    serializer_class = PostSerializer