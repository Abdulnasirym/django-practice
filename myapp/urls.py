from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('questions/', views.question_list, name='question_list'),
	path('questions/<int:id>/', views.question_detail, name='question_detail'),
	path('questions/add/', views.add_question, name='add_question'),
	path('tasks/', views.task_list, name='task_list'),
	path('tasks/<int:id>/', views.task_detail, name='task_detail'),
	path('tasks/add/', views.add_task, name='add_task'),
]