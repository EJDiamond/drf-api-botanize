from django.db.models import Count
from django.shortcuts import render
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Answer
from .serializers import AnswerSerializer, AnswerDetailSerializer


class AnswerList(generics.ListCreateAPIView):
    serializer_class = AnswerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Answer.objects.annotate(
        like_count=Count('likes', distinct=True),
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'post'
    ]
    ordering_fields = [
        'like_count',
    ]

    def perform_create(self, serializer):
        """
        Makes sure the answer is associated to a user
        """
        serializer.save(owner=self.request.user)


class AnswerDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Enables owner to edit and delete their answer
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = AnswerDetailSerializer
    queryset = Answer.objects.annotate(
        like_count=Count('likes', distinct=True),
    ).order_by('-created_at')
