from django.db.models import Count
from django.shortcuts import render
from rest_framework import generics, permissions, filters
from .models import Post
from .serializers import PostSerializer
from drf_api.permissions import IsOwnerOrReadOnly


class PostList(generics.ListCreateAPIView):
    """
    Create lists of posts which are read only if the user is not authenticated
    """
    serializer_class = PostSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.annotate(
        bookmark_count=Count('bookmarks', distinct=True)
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
    ]

    ordering_fields = [
        'bookmark_count',
    ]

    def perform_create(self, serializer):
        """
        Associates post with logged in user
        """
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Only posts owner can edit or delete it
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.all()
