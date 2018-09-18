from django.shortcuts import render
from django.db.models import Avg
from temp_test.models import Dataset


def history_data(request,pk):
	data = Dataset.objects.filter(grow_id=pk)
	avg_in_temp = data.aggregate(Avg('inside_temperature'))
	avg_in_humidity = data.aggregate(Avg('inside_humidity'))

	avg_out_temp = data.aggregate(Avg('outside_temperature'))
	avg_out_humidity = data.aggregate(Avg('outside_humidity'))

	avg_water_temp = data.aggregate(Avg('water_temperature'))
	avg_water_pH = data.aggregate(Avg('water_pH'))




	in_temp_data = []
	in_hum_data = []
	out_temp_data = []
	out_hum_data = []
	water_temp_data = []
	water_ph_data = []
	for d in data:
		in_temp_data.append(d.inside_temperature)
		in_hum_data.append(d.inside_humidity)
		out_temp_data.append(d.outside_temperature)
		out_hum_data.append(d.outside_humidity)
		water_temp_data.append(d.water_temperature)
		water_ph_data.append(d.water_pH)

	print(water_ph_data)
	template_name = 'temp_test/history_data.html'
	return render(request, template_name, {'data': data, 'water_ph_data': water_ph_data, 'water_temp_data': water_temp_data, 'out_hum_data':out_hum_data,'out_temp_data': out_temp_data,'in_hum_data': in_hum_data, 'in_temp_data': in_temp_data, 'avg_in_temp': avg_in_temp, 'avg_in_humidity': avg_in_humidity,'avg_out_temp': avg_out_temp, 'avg_out_humidity': avg_out_humidity, 'avg_water_temp': avg_water_temp, 'avg_water_pH': avg_water_pH})



