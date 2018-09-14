from django.shortcuts import render
from temp_test.models import Grow
from datetime import datetime
from django.utils import timezone
import pytz

def stop_grow(request, pk):
	print('stopgrow line 8:stopped grow test!!', pk)
	#data = Dataset.objects.filter(grow_id=pk).order_by('-id')[:1]
	grow = Grow.objects.get(pk=pk)
	print('stopgrow line 8', grow)
	today = datetime.today()
	grow.end_date = today
	#data = Grow(end_date=today)
	grow.save()

	template_name = 'temp_test/stop_grow.html'
	return render(request, template_name, {'grow': grow})