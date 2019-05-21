from django.db import models
from django.shortcuts import reverse

# Create your models here.
class Video(models.Model):
    name = models.CharField(max_length=40)
    genre = models.CharField(max_length=20)
    file = models.FileField()


    def get_absolute_url(self):
        return reverse('vidapp:video')

    def __str__(self):
        return self.name

