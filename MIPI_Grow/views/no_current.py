from django.shortcuts import render
from MIPI_Grow.models import Grow
from datetime import datetime
from django.utils import timezone
import pytz

def no_current(request):
	template = 'MIPI_Grow/no_current.html'
	return render(request, template)