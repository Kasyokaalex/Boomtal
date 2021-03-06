from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Album(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=25)
	genre = models.CharField(max_length=15)
	cover = models.FileField()

	def __str__(self):
		return self.name


class Song(models.Model):
	album = models.ForeignKey(Album, on_delete=models.CASCADE)
	song_name = models.CharField(max_length=25)
	song_file = models.FileField()

	def __str__(self):
		return self.song_name
