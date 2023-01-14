from django.shortcuts import render
from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Answer
from .serializers import AnswerSerializer, AnswerDetailSerializer


class AnswerList(generics.ListCreateAPIView):
    serializer_class = AnswerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Answer.objects.all()

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
    queryset = Answer.objects.all()
