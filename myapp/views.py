from django.shortcuts import render, get_object_or_404
from .models import Question

# Create your views here.
def home(request):
	return render(request, 'home.html')

def question_list(request):
	questions = Question.objects.all()
	return render(request, 'question_list.html', {'questions': questions})

def question_detail(request, id):
	question = get_object_or_404(Question, id=id)
	return render(request, 'question_detail.html', {'question': question})