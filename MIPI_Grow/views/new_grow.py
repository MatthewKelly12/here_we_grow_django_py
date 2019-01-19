from django.shortcuts import render
from MIPI_Grow.models import Grow
from MIPI_Grow.forms import NewGrowForm
from .start_grow import start_grow
from .stop_grow import stop_grow

def new_grow(request):

	if request.method == 'GET':
		grow_form = NewGrowForm()
		template_name = 'MIPI_Grow/new_grow.html'
		return render(request, template_name, {'grow_form': grow_form})

	elif request.method == 'POST':
		grow_form = NewGrowForm(data=request.POST)

		if grow_form.is_valid():
			grow = grow_form.save(commit=False)
			grow.user = request.user
			grow.save()
			print(grow.id)
			start_grow(request, grow.id)
		template_name = 'MIPI_Grow/new_grow.html'
		return render(request, template_name, {'grow_form': grow_form})