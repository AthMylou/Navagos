from django.shortcuts import render

from .models import Question, Answer, QuestionAnswer

# Create your views here.

def index(request):
    """The home page of Navagos"""
    return render(request, 'navagos_main/index.html')

def questions(request):
    """Shows all questions."""
    questions = Question.objects.order_by('id')
    context = {'questions':questions}
    return render(request, 'navagos_main/questions.html', context)

def question(request, question_id):
    """Shows a single question and all its answers"""
    question = Question.objects.get(id = question_id)
    answers = Answer.objects.order_by('id')
    question_answers = []
    
    for answer in answers:
        if answer.question == question:
            question_answers.append(answer)
               
    context = {'question':question, 'question_id': question_id, 'question_answers':question_answers}
    return render(request, 'navagos_main/question.html', context)
    
    
def about(request):
    """Shows the about page"""
    return render(request, 'navagos_main/about.html')