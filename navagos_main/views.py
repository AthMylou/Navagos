from django.shortcuts import render

from .models import Question

# Create your views here.

def index(request):
    """The home page of Navagos"""
    return render(request, 'navagos_main/index.html')

def questions(request):
    """Shows all questions."""
    questions = Question.objects.order_by('question_text')
    context = {'questions':questions}
    return render(request, 'navagos_main/questions.html', context)

def about(request):
    """Shows the about page"""
    return render(request, 'navagos_main/about.html')