from django.shortcuts import render, redirect


def index(request):
	if request.user.is_authenticated:

		return render(request, 'MIPI_Grow/home.html')
	else:
		return redirect('login')