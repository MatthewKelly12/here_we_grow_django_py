from django.shortcuts import render
from temp_test.models import Dataset


def history_data(request,pk):
	data = Dataset.objects.filter(grow_id=pk).order_by('-id')
	#print(data[20].outside_temperature)

	total_inside_temp = 0
	total_inside_humidity = 0
	total_outside_temp = 0
	total_outside_humidity = 0
	total_water_temp = 0
	total_water_ph = 0
	length = 0
	average = 0
	for dataset in data:
		total_outside_temp += dataset.outside_temperature
		length = len(data)
		average = (total_outside_temp)/(length)
		print(average)
	print(average)

	#prop_total = 0
	#prop_length = 0
		#prop_total += value
		#prop_length += 1
		#average = (prop_total)/(prop_length)











	template_name = 'temp_test/history_data.html'
	return render(request, template_name, {'data': data})
