from django.shortcuts import render
from .models import Dataset
import time
import datetime
import sqlite3


def index(request):
	return render(request, 'temp_test/index.html')

def stats(request):
	return render(request, 'temp_test/stats.html')


def run(self):
	while True:
		d = Dataset(grow='1',inside_temperature='77.6', inside_humidity='50.3', outside_temperature='89', outside_humidity='55', water_temperature='75.1', water_pH='77.6', image='pic')
		d.save()
		print(d)
		time.sleep(5)
	#return render('temp_test/run.html')



