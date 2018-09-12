from django.shortcuts import render
from temp_test.models import Grow
from datetime import datetime
from django.utils import timezone
import pytz


def current_grows(request):
	#day = datetime.date
	utc = pytz.UTC
	today = datetime.today()
	print(today)
	now = timezone.now()
	#print(day)
	current_grows = []
	grows = Grow.objects.filter(user=request.user.id)
	for grow in grows:
		if grow.end_date > utc.localize(today):
			current_grows.append(grow)
			print(grow.end_date)
			template_name = 'temp_test/current_grows.html'
	return render(request, template_name, {'grows': current_grows})