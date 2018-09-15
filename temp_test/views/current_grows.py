from django.shortcuts import render
from temp_test.models import Grow
from datetime import datetime
from django.utils import timezone
import pytz







def current_grows(request):
	utc = pytz.UTC
	today = datetime.today()

	now = timezone.now()
	current_grows = []
	print(f'current grows 19: working')

	grows = Grow.objects.filter(user=request.user.id).order_by('-id')


	if (grows.exists() == False):
			template_name = 'temp_test/no_current.html'
			return render(request, template_name)

	for grow in grows:

		if (grow.end_date == None):
			current_grows.append(grow)
			template_name = 'temp_test/current_grows.html'
			return render(request, template_name, {'grows': current_grows})
		else:
			template_name = 'temp_test/no_current.html'
			return render(request, template_name)

	#> utc.localize(today)