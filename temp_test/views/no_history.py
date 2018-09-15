from django.shortcuts import render
from temp_test.models import Grow
from datetime import datetime
from django.utils import timezone
import pytz

def no_history(request):
	template = 'temp_test/no_history.html'
	return render(request, template)