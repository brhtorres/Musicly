from django.db import models

class Music (models.Model):
	music_id = models.AutoField(primary_key=True)
	music_name = models.CharField(max_length = 50)
	music_singer = models.CharField(max_length = 50)
	like = models.BooleanField()

	def save_music(self):
		self.save()

	def __str__(self):
		return self.music_name

class Playlist (models.Model):
	playlist_id = models.AutoField(primary_key=True)
	playlist_name = models.CharField(max_length = 50)
	musics = models.ManyToManyField(Music)

	def save_playlist(self):
		self.save()

	def __str__(self):
		return self.playlist_name