from django.shortcuts import render
from drf_api.permissions import IsOwnerOrReadOnly
from rest_framework import generics, permissions, filters
from .models import Plant
from .serializers import PlantSerializer


class PlantList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = PlantSerializer
    queryset = Plant.objects.all().order_by('-created_at')
    search_fields = [
        'plant_name',
        'plant_type',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PlantDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = PlantSerializer
    queryset = Plant.objects.all().order_by('-created_at')
