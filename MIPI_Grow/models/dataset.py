from django.db import models
from django.utils import timezone
from .grow import Grow

class Dataset(models.Model):
	grow = models.ForeignKey(Grow, on_delete=models.CASCADE)
	inside_temperature = models.IntegerField()
	inside_humidity = models.IntegerField()
	outside_temperature = models.IntegerField()
	outside_humidity = models.IntegerField()
	water_temperature = models.IntegerField()
	water_pH = models.IntegerField()
	date = models.DateTimeField(default=timezone.now)
	image = models.TextField(max_length=200)

	def __str__(self):
		return str(self.grow)
