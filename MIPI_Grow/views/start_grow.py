from MIPI_Grow.models import Dataset, Grow
from MIPI_Grow.pi_functions.pi_functions import get_am2302, get_water_temp, get_water_ph

# COMMENTED OUT DEPENDENCIES FOR TESTING WITHOUT RASPBERRY PI
#import Adafruit_DHT
#import RPi.GPIO as GPIO
import subprocess
import time
import datetime
import requests
from time import sleep
from .stop_grow import stop_grow




def start_grow(request,growid):
	counter = 0
	url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&APPID=447afc2326760172ae872c6a9c4f3169'
	while True:
		grow = Grow.objects.get(pk=growid)

		counter += 1
		print(counter)
		img_name = (str(grow.name) + str(counter))
		img_filename = ("MIPI_Grow/static/MIPI_Grow/images/"+img_name+".jpeg")
		#print(img_name)
		print(img_filename)
		#subprocess.call(['raspistill', '-o', img_filename])

		# Get data from temp/humdity sensor
		indoor_humidity, indoor_temperature = get_am2302()

		#Get data from water temp sensor
		water_temperature = get_water_temp()

		#Get data from water temp sensor
		water_pH = get_water_ph()




		print("water ph and temp", water_temperature, water_pH)

		city = 'Nashville'
		r = requests.get(url.format(city)).json()
		out_temp = r['main']['temp']
		out_humidity = r['main']['humidity']


		print("INDOOR TEMP", indoor_temperature)
		print("INDOOR HUMIDITY", indoor_humidity)
		print ("OUTDOOR TEMP", out_temp)
		print("OUTDOOR HUMIDITY", out_humidity)
		#print(dataset)

		d = Dataset(
			inside_temperature=indoor_temperature,
			inside_humidity=indoor_humidity,
			outside_temperature=out_temp,
			outside_humidity=out_humidity,
			water_temperature=water_temperature,
			water_pH=water_pH,
			image=img_name,
			grow_id=growid
		)

		d.save()
		time.sleep(5)


		if (grow.end_date is not None):
			print('GROW STOPPED')
			break




