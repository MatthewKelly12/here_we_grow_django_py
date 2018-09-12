from django.shortcuts import render
from temp_test.models import Grow
from temp_test.forms import NewGrowForm

def new_grow(request):

	if request.method == 'GET':
		grow_form = NewGrowForm()
		template_name = 'temp_test/new_grow.html'
		return render(request, template_name, {'grow_form': grow_form})

	elif request.method == 'POST':
		grow_form = NewGrowForm(data=request.POST)

		if grow_form.is_valid():
			grow = grow_form.save(commit=False)
			grow.user = request.user
			grow.save()
		template_name = 'temp_test/new_grow.html'
		return render(request, template_name, {'grow_form': grow_form})