from django.db import models
from django.utils import timezone
from .grow import Grow

class Dataset(models.Model):
	grow = models.ForeignKey(Grow, on_delete=models.CASCADE)
	inside_temperature = models.CharField(max_length=50)
	inside_humidity = models.CharField(max_length=50)
	outside_temperature = models.CharField(max_length=50)
	outside_humidity = models.CharField(max_length=50)
	water_temperature = models.CharField(max_length=50)
	water_pH = models.CharField(max_length=50)
	date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return str(self.grow)
