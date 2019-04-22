# COMMENTED OUT DEPENDENCIES FOR TESTING WITHOUT RASPBERRY PI
#import Adafruit_DHT
#import RPi.GPIO as GPIO
import requests
# COMMENTED OUT FOR TESTING WITHOUT RASPBERRY PI
#GPIO.setwarnings(False)
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(4, GPIO.IN)

# Functions that require the Raspberry PI

def get_pic(img_name):
	img_filename = ("MIPI_Grow/static/MIPI_Grow/images/"+img_name+".jpeg")
	# COMMENTED OUT FOR TESTING WITHOUT RASPBERRY PI
	#subprocess.call(['raspistill', '-o', img_filename])
	return img_filename

def get_am2302():
	# COMMENTED OUT FOR TESTING WITHOUT RASPBERRY PI
	#indoor_humidity, indoor_temperature = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, 4)
	#if indoor_humidity is not None and indoor_temperature is not None:
	#indoor_humidity = round(indoor_humidity, 2)
	#indoor_temperature = round(indoor_temperature*1.8 + 32, 2)

	indoor_humidity = 32
	indoor_temperature = 88
	return (indoor_humidity,indoor_temperature)

def get_weather(url):

	city = 'Nashville'
	r = requests.get(url.format(city)).json()
	out_temp = r['main']['temp']
	out_humidity = r['main']['humidity']

	return (out_temp, out_humidity)


def get_water_temp():
	water_temp = 75.1

	return water_temp

def get_water_ph():
	water_ph = 6.7

	return water_ph

