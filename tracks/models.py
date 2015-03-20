from django.db import models

# Create your models here.

class Track(models.Model):
	name = models.CharField(max_length=50)
	cover = models.ImageField(upload_to='covers/')
	top_color = models.CharField(max_length=7)
	bottom_color = models.CharField(max_length=7)

	def __str__(self):
		return "{0}".format(self.name)


class Step(models.Model):
	track = models.ForeignKey('tracks.Track')
	cover = models.ImageField(upload_to='step-cover/')
	name = models.CharField(max_length=100)
	url = models.URLField()

	def __str__(self):
		return "{0} - {1}".format(self.track.name, self.name)

