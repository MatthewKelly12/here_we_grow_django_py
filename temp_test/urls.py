from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
	path('run/', views.run, name='run'),
	path('stats/', views.stats, name='stats'),
]