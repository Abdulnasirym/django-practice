from django import forms
from .models import Question, Task
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class QuestionForm(forms.ModelForm):
	class Meta:
		model = Question
		fields = ['title', 'body']

class TaskForm(forms.ModelForm):
	class Meta:
		model = Task
		fields = ['title', 'description', 'completed']

class SignUpForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

