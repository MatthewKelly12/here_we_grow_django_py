# COMMENTED OUT FOR TESTING WITHOUT RASPBERRY PI
#GPIO.setwarnings(False)
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(4, GPIO.IN)

# Functions that require the Raspberry PI

def get_pic(img_name):
	# COMMENTED OUT FOR TESTING WITHOUT RASPBERRY PI
	img_filename = ("MIPI_Grow/static/MIPI_Grow/images/"+img_name+".jpeg")
	#subprocess.call(['raspistill', '-o', img_filename])
	return img_filename

def get_am2302():
	# COMMENTED OUT FOR TESTING WITHOUT RASPBERRY PI
	#indoor_humidity, indoor_temperature = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, 4)
	#if indoor_humidity is not None and indoor_temperature is not None:
	#indoor_humidity = round(indoor_humidity, 2)
	#indoor_temperature = round(indoor_temperature*1.8 + 32, 2)
	#indoor_temperature = 77.2
	#indoor_humidity = 54
	indoor_humidity = 32
	indoor_temperature = 88
	return (indoor_humidity,indoor_temperature)

def get_water_temp():

	return 75.1

def get_water_ph():

	return 6.7

