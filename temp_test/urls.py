from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
	path('start_grow/', views.start_grow, name='start_grow'),
	path('register/', views.register, name='register'),
	path('logout/', views.user_logout, name='logout'),
	path('current_grows/', views.current_grows, name='current_grows'),
	path('current_data/<int:pk>', views.current_data, name='current_data'),
	path('new_grow/', views.new_grow, name='new_grow'),
	path('history_grows/', views.history_grows, name='history_grows'),
	path('history_data/<int:pk>', views.history_data, name='history_data')
]