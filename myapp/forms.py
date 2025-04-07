from django import forms
from .models import Question, Task

class QuestionForm(forms.ModelForm):
	class Meta:
		model = Question
		fields = ['title', 'body']

class TaskForm(forms.ModelForm):
	class Meta:
		model = Task
		fields = ['title', 'description', 'completed']
	