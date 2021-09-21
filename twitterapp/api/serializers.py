from rest_framework import serializers
from twitterapp.models import post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = post
        fields = "__all__"