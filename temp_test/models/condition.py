from django.db import models
from .type import Type
from .variety import Variety



class Condition(models.Model):
	temperature = models.CharField(max_length=100)
	humidity = models.CharField(max_length=100)
	pH = models.CharField(max_length=100)
	type = models.ForeignKey(Type, on_delete=models.CASCADE)
	variety = models.ForeignKey(Variety, on_delete=models.CASCADE)

	def __str__(self):
		return (f'{self.variety} {self.type}')