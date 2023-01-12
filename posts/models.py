from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):

    plant_type_choices = [
        ('palms', 'Palms'),
        ('ferns', 'Ferns'),
        ('indoor_trees', 'Indoor trees'),
        ('cacti_and_succulents', 'Cacti and Succulents'),
        ('hydroculture', 'Hydroculture'),
        ('foliage plants', 'Foliage plants'),
        ('bonsai', 'Bonsai')
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    plant_type = models.CharField(
        max_length=32, choices=plant_type_choices, default='normal'
    )
    plant = models.CharField(max_length=255)
    question = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../plant-image_oljnkv', blank=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.plant}'
