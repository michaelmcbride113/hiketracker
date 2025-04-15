from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Hike(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    difficulty = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('hike-detail', kwargs={'hike_id': self.id})