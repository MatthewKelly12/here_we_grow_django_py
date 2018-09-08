from django.db import models
from .category import Category



class Variety(models.Model):
	name = models.CharField(max_length=100)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)

	def __str__(self):
		return self.name