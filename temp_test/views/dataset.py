from django.shortcuts import render, redirect
from temp_test.models import Dataset
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
#import Adafruit_DHT
#import RPi.GPIO as GPIO
import subprocess
import time
import datetime
import sqlite3
import requests

#GPIO.setwarnings(False)
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(4, GPIO.IN)


def index(request):
	if request.user.is_authenticated:

		return render(request, 'temp_test/home.html')
	else:
		return redirect('login')


def stats(request):
	return render(request, 'temp_test/stats.html')


def	register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)


		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			return redirect('index')
	else:
		form = UserCreationForm()

	context = {'form': form}
	return render(request, 'registration/register.html', context)


def user_logout(request):
	logout(request)
	return redirect('login')





def run(self):
	while True:
		#indoor_humidity, indoor_temperature = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, 4)
		#if indoor_humidity is not None and indoor_temperature is not None:
		#indoor_humidity = round(indoor_humidity, 2)
		#indoor_temperature = round(indoor_temperature, 2)
		indoor_temperature = 77.2
		indoor_humidity = 54
		print(indoor_temperature*1.8 + 32)
		print(indoor_humidity)



		url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&APPID=447afc2326760172ae872c6a9c4f3169'
		city = 'Nashville'
		r = requests.get(url.format(city)).json()
		out_temp = r['main']['temp']
		out_humidity = r['main']['humidity']

		print(out_temp)
		print(out_humidity)

		d = Dataset(grow='1',inside_temperature=indoor_temperature, inside_humidity=indoor_humidity, outside_temperature=out_temp, outside_humidity=out_humidity, water_temperature='75.1', water_pH='77.6', image='pic')
		d.save()
		print(d)
		time.sleep(5)
	#return render('temp_test/run.html')



