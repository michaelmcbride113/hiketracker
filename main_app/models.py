from django.db import models

class Hike(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    difficulty = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.name