from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
	path('', views.home, name='home'),
	path('questions/', views.question_list, name='question_list'),
	path('questions/<int:id>/', views.question_detail, name='question_detail'),
	path('questions/add/', views.add_question, name='add_question'),
	path('tasks/', views.task_list, name='task_list'),
	path('tasks/<int:id>/', views.task_detail, name='task_detail'),
	path('tasks/add/', views.add_task, name='add_task'),
	path('questions/<int:question_id>/edit/', views.edit_question, name='edit_question'),
	path('questions/<int:question_id>/delete>/', views.delete_question, name='delete_question'),	
	path('register/', views.register, name='register'),
	path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
	path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
	path('accounts/profile/', views.question_list, name='question_list'),
]