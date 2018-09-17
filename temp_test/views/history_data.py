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

	print('LINE 21HD', avg_in_temp)
	print(avg_in_humidity)
	print(avg_out_temp)
	print(avg_out_humidity)
	print(avg_water_temp)
	print(avg_water_pH)

	dataset = []
	dataset.append(avg_in_temp)
	dataset.append(avg_in_humidity)
	dataset.append(avg_out_temp)
	dataset.append(avg_out_humidity)
	dataset.append(avg_water_temp)
	dataset.append(avg_water_pH)
	print(dataset)




	template_name = 'temp_test/history_data.html'
	return render(request, template_name, {'dataset': dataset})



