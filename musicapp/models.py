from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Song(models.Model):
    name = models.CharField(max_length=200)
    album = models.CharField(max_length=200)
    song_img = models.FileField()
    year = models.IntegerField()
    singer = models.CharField(max_length=200)
    song_file = models.FileField()

    def __str__(self):
        return self.name


class Playlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    playlist_name = models.CharField(max_length=200)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
