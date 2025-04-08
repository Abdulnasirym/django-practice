from django.shortcuts import render, get_object_or_404
from .models import Question, Task
from .forms import QuestionForm, TaskForm
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def home(request):
	return render(request, 'home.html')

def question_list(request):
	questions = Question.objects.all()
	return render(request, 'question_list.html', {'questions': questions})

def question_detail(request, id):
	question = get_object_or_404(Question, id=id)
	return render(request, 'question_detail.html', {'question': question})

def task_list(request):
	tasks = Task.objects.all()
	return render(request, 'task_list.html', {'tasks': tasks})

def task_detail(request, id):
	task = get_object_or_404(Task, id=id)
	return render(request, 'task_detail.html', {'task': task})

def add_question(request):
	if request.method == 'POST':
		form = QuestionForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('question_list'))
	else:
		form = QuestionForm()

	return render(request, 'add_question.html', {'form': form})

def add_task(request):
	if request.method == 'POST':
		form = TaskForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('task_list'))
	else:
		form = TaskForm()

	return render(request, 'add_task.html', {'form': form})

def edit_question(request, question_id):
	question = get_object_or_404(Question, pk=question_id)

	if request.method == 'POST':
		form = QuestionForm(request.POST, instance=question)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('question_list'))
	else:
		form = QuestionForm(instance=question)

	return render(request, 'edit_question.html', {'form': form})