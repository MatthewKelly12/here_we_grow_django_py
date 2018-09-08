from django.shortcuts import render
from .models import Dataset
import time
import datetime
import sqlite3
import requests


def index(request):
	return render(request, 'temp_test/index.html')

def stats(request):
	return render(request, 'temp_test/stats.html')


def run(self):
	while True:
		url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&APPID=447afc2326760172ae872c6a9c4f3169'
		city = 'Nashville'
		r = requests.get(url.format(city)).json()
		out_temp = r['main']['temp']
		out_humidity = r['main']['humidity']
		print(out_temp)
		print(out_humidity)
		d = Dataset(grow='1',inside_temperature='77.6', inside_humidity='50.3', outside_temperature=out_temp, outside_humidity=out_humidity, water_temperature='75.1', water_pH='77.6', image='pic')
		d.save()
		print(d)
		time.sleep(5)
	#return render('temp_test/run.html')



