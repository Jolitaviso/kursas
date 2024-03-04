from django.shortcuts import render

from .models import Post, PostLike, Comment, CommentLike
from .serializers import PostSerializer
from . import models, serializers
from rest_framework import generics, permissions

class PostList(generics.ListCreateAPIView):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)