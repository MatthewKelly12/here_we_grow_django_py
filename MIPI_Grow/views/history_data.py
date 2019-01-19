from django.shortcuts import render
from django.db.models import Avg
from MIPI_Grow.models import Dataset, Grow


def history_data(request,pk):
	data = Dataset.objects.filter(grow_id=pk)
	grow = Grow.objects.filter(id=pk)


	avg_in_temp = data.aggregate(Avg('inside_temperature'))
	avg_in_humidity = data.aggregate(Avg('inside_humidity'))

	avg_out_temp = data.aggregate(Avg('outside_temperature'))
	avg_out_humidity = data.aggregate(Avg('outside_humidity'))

	avg_water_temp = data.aggregate(Avg('water_temperature'))
	avg_water_pH = data.aggregate(Avg('water_pH'))

	start = 0
	end = 0
	for g in grow:
		start = g.start_date
		end = g.end_date

	in_temp_data = []
	in_hum_data = []
	out_temp_data = []
	out_hum_data = []
	water_temp_data = []
	water_ph_data = []
	img_date_data = []
	img = []
	counter = 0
	count = []
	name = 0
	for d in data:
		in_temp_data.append(d.inside_temperature)
		in_hum_data.append(d.inside_humidity)
		img.append(d.image)
		name = d.grow

		out_temp_data.append(d.outside_temperature)
		out_hum_data.append(d.outside_humidity)
		water_temp_data.append(d.water_temperature)
		water_ph_data.append(d.water_pH)
		img_date_data.append(d.date)
		counter += 1
		count.append(counter)


	template_name = 'MIPI_Grow/history_data.html'
	return render(request, template_name, {'img': img,'end': end,'start': start,'data': data, 'name': name, 'count': count, 'water_ph_data': water_ph_data, 'water_temp_data': water_temp_data, 'out_hum_data':out_hum_data,'out_temp_data': out_temp_data,'in_hum_data': in_hum_data, 'in_temp_data': in_temp_data, 'avg_in_temp': avg_in_temp, 'avg_in_humidity': avg_in_humidity,'avg_out_temp': avg_out_temp, 'avg_out_humidity': avg_out_humidity, 'avg_water_temp': avg_water_temp, 'avg_water_pH': avg_water_pH, 'img_date_data': img_date_data})



