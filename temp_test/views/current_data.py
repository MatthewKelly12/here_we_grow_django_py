from django.shortcuts import render
from temp_test.models import Dataset

def current_data(request,pk):
	data = Dataset.objects.filter(grow_id=pk).order_by('-id')[:1]
	template_name = 'temp_test/current_data.html'
	return render(request, template_name, {'data': data})