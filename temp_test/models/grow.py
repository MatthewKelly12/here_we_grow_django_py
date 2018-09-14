from django.db import models
from .condition import Condition
from .category import Category
from .variety import Variety
from .type import Type
from django.contrib.auth.models import User




class Grow(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	variety = models.ForeignKey(Variety, on_delete=models.CASCADE)
	type = models.ForeignKey(Type, on_delete=models.CASCADE)
	start_date = models.DateTimeField(auto_now_add=True)
	end_date = models.DateTimeField(auto_now=False, auto_now_add=False, null=True)
	description = models.TextField(max_length=200)

	def __str__(self):
		return self.name