from temp_test.models import Dataset, Grow
#import Adafruit_DHT
#import RPi.GPIO as GPIO
import subprocess
import time
import datetime
import requests
from time import sleep


#GPIO.setwarnings(False)
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(4, GPIO.IN)


def start_grow(request,growid):
	grow = Grow.objects.get(pk=growid)
	while True:

		img_filename = '/home/pi/projects/here_we_grow_django_py/temp_test/static/grow{counter}.jpeg'
		subprocess.call(['raspistill', '-o', img_filename])


		#indoor_humidity, indoor_temperature = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, 4)
		#if indoor_humidity is not None and indoor_temperature is not None:
		#indoor_humidity = round(indoor_humidity, 2)
		#indoor_temperature = round(indoor_temperature, 2)
		indoor_temperature = '77.2'
		indoor_humidity = '54'
		#print(f'Name: {name}')
		print(f'Indoor Temp: {indoor_temperature}')
		print(f'Indoor Humidity: {indoor_humidity}')
		water_temperature='75.1'
		water_pH='77.6'
		image='pic'



		url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&APPID=447afc2326760172ae872c6a9c4f3169'
		city = 'Nashville'
		r = requests.get(url.format(city)).json()
		out_temp = r['main']['temp']
		out_humidity = r['main']['humidity']

		print(f'Outdoor Temp: {out_temp}')
		print(f'Outdoor Humdity: {out_humidity}')
		#print(dataset)

		d = Dataset(inside_temperature=indoor_temperature, inside_humidity=indoor_humidity, outside_temperature=out_temp, outside_humidity=out_humidity, water_temperature='75.1', water_pH='77.6', image='pic', grow_id=growid)
		d.save()
		time.sleep(5)
	#return render('temp_test/run.html')



