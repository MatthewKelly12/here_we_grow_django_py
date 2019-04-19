from django.shortcuts import render
from MIPI_Grow.models import Grow
from datetime import datetime
from django.utils import timezone
import pytz


def history_grows(request):
	utc = pytz.UTC
	today = datetime.today()
	now = timezone.now()
	history_grows = []
	grows = Grow.objects.filter(user=request.user.id).order_by('-id')

	if (grows.exists() == False):
			template_name = 'MIPI_Grow/no_history.html'
			return render(request, template_name)

	for grow in grows:
		if grow.end_date:
			history_grows.append(grow)
			#print(f'Name: {grow.name}')
			#print(f'Start Date: {grow.start_date}')
			#print(f'End Date: {grow.end_date}')
	template_name = 'MIPI_Grow/history_grows.html'
	return render(request, template_name, {'grows': history_grows})
		#else:
			#template_name = 'MIPI_Grow/no_history.html'
			#return render(request, template_name)

	#< utc.localize(today)