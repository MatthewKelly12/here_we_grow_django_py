from django.shortcuts import render, redirect


def index(request):
	if request.user.is_authenticated:

		return render(request, 'temp_test/home.html')
	else:
		return redirect('login')