from django.shortcuts import render
from temp_test.models import Grow
from datetime import datetime
from django.utils import timezone
import pytz


def history_grows(request):
	utc = pytz.UTC
	today = datetime.today()
	now = timezone.now()
	history_grows = []
	grows = Grow.objects.filter(user=request.user.id)
	for grow in grows:
		if grow.end_date < utc.localize(today):
			history_grows.append(grow)
			print(grow.end_date)
			template_name = 'temp_test/history_grows.html'
	return render(request, template_name, {'grows': history_grows})