from temp_test.models import Dataset, Grow
import Adafruit_DHT
import RPi.GPIO as GPIO
import subprocess
import time
import datetime
import requests
from time import sleep
from .stop_grow import stop_grow


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)


def start_grow(request,growid):
	counter = 0
	while True:
		grow = Grow.objects.get(pk=growid)

		counter += 1
		print(counter)
		img_name = (str(grow.name) + str(counter))
		img_filename = ("temp_test/static/temp_test/images/"+img_name+".jpeg")
		print(img_name)
		print(img_filename)
		subprocess.call(['raspistill', '-o', img_filename])


		indoor_humidity, indoor_temperature = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, 4)
		#if indoor_humidity is not None and indoor_temperature is not None:
		indoor_humidity = round(indoor_humidity, 2)
		indoor_temperature = round(indoor_temperature*1.8 + 32, 2)
		#indoor_temperature = '77.2'
		#indoor_humidity = '54'
		#print(f'Name: {name}')
		print("INDOOR TEMP", indoor_temperature)
		print("INDOOR HUMIDITY", indoor_humidity)
		
		
		water_temperature='75.1'
		water_pH='77.6'




		url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&APPID=447afc2326760172ae872c6a9c4f3169'
		city = 'Nashville'
		r = requests.get(url.format(city)).json()
		out_temp = r['main']['temp']
		out_humidity = r['main']['humidity']
		out_temp = str(out_temp)
		out_humidity =str(out_humidity)

		print ("OUTDOOR TEMP", out_temp)
		print("OUTDOOR HUMIDITY", out_humidity)
		#print(dataset)

		d = Dataset(inside_temperature=indoor_temperature, inside_humidity=indoor_humidity, outside_temperature=out_temp, outside_humidity=out_humidity, water_temperature='75.1', water_pH='77.6', image=img_name, grow_id=growid)
		d.save()
		time.sleep(5)
		

		if (grow.end_date is not None):
			print('GROW STOPPED')
			break
	



