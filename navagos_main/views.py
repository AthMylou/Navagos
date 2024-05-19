from django.shortcuts import render

from .models import Question, Answer, QuestionAnswer, Category

# Create your views here.

def index(request):
    """The home page of Navagos"""
    return render(request, 'navagos_main/index.html')

def categories(request):
    """Shows all categories"""
    categories = Category.objects.order_by('id')
    context = {'categories' :categories}
    return render(request, 'navagos_main/categories.html', context)

def category(request, category_id):
    """Shows a single category and all its questions"""
    category = Category.objects.get(id = category_id)
    questions = Question.objects.order_by('id')
    category_questions = []
    
    for question in questions:
        if question.category == category:
            category_questions.append(question)
            question_id = question.id
    
    context = {'category':category, 'category_id': category_id, 'category_questions':category_questions, 'question_id':question_id}
    return render(request, 'navagos_main/category.html', context)


def questions(request):
    """Shows all questions."""
    questions = Question.objects.order_by('id')
    context = {'questions':questions}
    return render(request, 'navagos_main/questions.html', context)

def question(request, question_id):
    """Shows a single question and all its answers"""
    question = Question.objects.get(id = question_id)
    answers = Answer.objects.filter(question = question)
    values = QuestionAnswer.objects.filter(question = question) 
    
    for item in values:
        if item.value == True:
            correct_answer = item.answer   
               
    context = {'question':question, 'question_id': question_id, 'answers':answers, 'correct_answer':correct_answer}
    return render(request, 'navagos_main/question.html', context)
    
    
def about(request):
    """Shows the about page"""
    return render(request, 'navagos_main/about.html')