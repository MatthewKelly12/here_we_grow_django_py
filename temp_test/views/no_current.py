from django.shortcuts import render
from temp_test.models import Grow
from datetime import datetime
from django.utils import timezone
import pytz

def no_current(request):
	template = 'temp_test/no_current.html'
	return render(request, template)