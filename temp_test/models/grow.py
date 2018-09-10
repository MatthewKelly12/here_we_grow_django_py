from django.db import models
from .condition import Condition
from django.contrib.auth.models import User




class Grow(models.Model):
	name = models.CharField(max_length=100)
	start_date = models.DateTimeField(auto_now=False, auto_now_add=False)
	end_date = models.DateTimeField(auto_now=False, auto_now_add=False)
	description = models.CharField(max_length=200)
	condition = models.ForeignKey(Condition, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.name