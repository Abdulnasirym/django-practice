from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('questions/', views.question_list, name='question_list'),
	path('questions/<int:id>/', views.question_detail, name='question_detail'),
]