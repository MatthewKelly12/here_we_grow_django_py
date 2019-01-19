from django.shortcuts import render
from MIPI_Grow.models import Grow
from datetime import datetime
from django.utils import timezone
import pytz

def no_history(request):
	template = 'MIPI_Grow/no_history.html'
	return render(request, template)