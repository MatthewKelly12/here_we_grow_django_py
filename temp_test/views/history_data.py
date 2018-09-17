from django.shortcuts import render
from django.db.models import Avg
from temp_test.models import Dataset


def history_data(request,pk):
	data = Dataset.objects.filter(grow_id=pk).order_by('-id')
	avg_in_temp = data.aggregate(Avg('inside_temperature'))
	avg_in_humidity = data.aggregate(Avg('inside_humidity'))

	avg_out_temp = data.aggregate(Avg('outside_temperature'))
	avg_out_humidity = data.aggregate(Avg('outside_humidity'))

	avg_water_temp = data.aggregate(Avg('water_temperature'))
	avg_water_pH = data.aggregate(Avg('water_pH'))

	# inT = []
	# inH = []
	# outT = []
	# outH = []
	# waterT = []
	# waterP = []
	# inT.append(avg_in_temp)
	# inH.append(avg_in_humidity)
	# outT.append(avg_out_temp)
	# outH.append(avg_out_humidity)
	# waterT.append(avg_water_temp)
	# waterP.append(avg_water_pH)

	template_name = 'temp_test/history_data.html'
	return render(request, template_name, {'avg_in_temp': avg_in_temp, 'avg_in_humidity': avg_in_humidity,'avg_out_temp': avg_out_temp, 'avg_out_humidity': avg_out_humidity, 'avg_water_temp': avg_water_temp, 'avg_water_pH': avg_water_pH})



