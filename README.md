
![](temp_test/static/temp_test/images/mypigrow_logo.png)

# MIPI GROW
MIPI Grow is a Django web application that uses a tiny Raspberry Pi computer and external sensors to monitor a small greenhouse. Users can register, log in, start new grows, and monitor their data. Once a grow is started, image data, inside temperature and humidity, and outside temperature and humidity are written to a sqlite3 database on a looping interval. The data is then displayed to the user with text, charts and images. Once a grow is stopped, it is logged to the history of grows where users can view their data points and data averages and watch a time lapse of their grow.

## Technologies Used
		Python
		Django
		JavaScript
		Raspberry Pi
		Sqlite3
		ChartsJS
		AdaFruit AM2302 Temperature and 			Humdity Sensor
		Raspberry Pi Camera
		OpenWeatherMap API
		[](https://openweathermap.org/api)