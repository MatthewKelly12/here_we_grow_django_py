from django.shortcuts import render
from temp_test.models import Grow


def current_grows(request):
	grows = Grow.objects.filter(user=request.user.id)
	template_name = 'temp_test/current_grows.html'
	return render(request, template_name, {'grows': grows})