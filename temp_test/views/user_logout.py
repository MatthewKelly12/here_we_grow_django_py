from django.shortcuts import render, redirect
from django.contrib.auth import logout


def user_logout(request):
	logout(request)
	return redirect('login')