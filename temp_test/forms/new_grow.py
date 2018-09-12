from django.contrib.auth.models import User
from django import forms
from temp_test.models import Grow


class NewGrowForm(forms.ModelForm):

	class Meta:
		model = Grow
		exclude = ['user']
		fields = ['name', 'condition', 'start_date', 'end_date', 'description']