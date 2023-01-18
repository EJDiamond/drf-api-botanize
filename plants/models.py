from django.db import models
from django.contrib.auth.models import User


class Plant(models.Model):

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
    plant_name = models.CharField(max_length=255)
    plant_type = models.CharField(
        max_length=32, choices=plant_type_choices, default='palms'
    )
    image = models.ImageField(
        upload_to='images/', default='../pots_pwjrw8', blank=True
    )
    age = models.IntegerField(blank=True)
    about = models.TextField(blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.owner} {self.plant_name}'
