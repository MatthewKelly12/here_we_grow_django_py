from django.shortcuts import render
from temp_test.models import Dataset, Grow

def current_data(request,pk):
	data = Dataset.objects.filter(grow_id=pk).order_by('-id')[:1]
	grow = Grow.objects.filter(id=pk)
	start = 0
	for g in grow:
		start = g.start_date

	print(start)
	template_name = 'temp_test/current_data.html'
	return render(request, template_name, {'data': data, 'start': start})