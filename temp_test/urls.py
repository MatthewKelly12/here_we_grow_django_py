from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
	path('start_grow/', views.start_grow, name='start_grow'),
	path('register/', views.register, name='register'),
	path('logout/', views.user_logout, name='logout'),
	path('current_grows/', views.current_grows, name='current_grows')
]