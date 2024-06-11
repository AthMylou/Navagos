from django.shortcuts import render, redirect

from datetime import datetime
from django.contrib.auth.decorators import login_required

from .models import Question, Answer, QuestionAnswer, Category, Test, TestQuestion
from .random_test import create_test

# Create your views here.

def index(request):
    """The home page of Navagos"""
    return render(request, 'navagos_main/index.html')

@login_required
def categories(request):
    """Shows all categories"""
    categories = Category.objects.order_by('id')
    context = {'categories' :categories}
    return render(request, 'navagos_main/categories.html', context)

@login_required
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

@login_required
def questions(request):
    """Shows all questions."""
    questions = Question.objects.order_by('id')
    context = {'questions':questions}
    return render(request, 'navagos_main/questions.html', context)

@login_required
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
    
@login_required    
def test(request):
    """Renders the page prompting user to take test"""
    print(request.user)
    print(type(request.user))
    return render(request, 'navagos_main/test.html')
@login_required
def new_test(request):
    """Produces a new test and renders its page"""
    questions = create_test()
    question_answers = {}
        
    for question in questions:
        answers = Answer.objects.filter(question = question)
        question_answers[question] = answers
            
    context = {'questions': questions, 'question_answers': question_answers}
    return render(request, 'navagos_main/new_test.html', context)

@login_required
def submit_test(request):
    """This view handles the results of a test"""
    selected_answers = {}
    correct_count = 0
    if request.method == 'POST':
        selections= {}
        user = request.user
        #create a Test model instance in the database    
        new_test = Test.objects.create(test_datetime = datetime.now(), pass_fail = False, correct_answers = correct_count, user = user)
        for index, (question, answer) in enumerate(request.POST.items()):
            # index = 0 represents the csrf token
            if index == 0:
                continue   
            #stores all selected questions and answers to a dictionary
            selections[question] = answer
            #for each question answered in the test create a TestQuestion model instance in the database
            question_id = int(question.split('_')[1]) 
            test_question = TestQuestion.objects.create(question = Question.objects.get(id = question_id), answered_correctly = False, test = new_test, chosen_answer = Answer.objects.get(id = answer))       
            test_question.save()     
            #count the correct answers and update the answered_correctly attribute in the database
            for item in QuestionAnswer.objects.filter(answer = answer):
                if item.value == True:
                    correct_count += 1 
                    
    new_test.correct_answers = correct_count
    if correct_count >= 47:
        new_test.pass_fail = True
    new_test.save()
    
    context = {"selected_answers": selected_answers, 'correct_count': correct_count}
    return redirect('navagos_main:results')


@login_required
def results(request):
    """Shows the test results"""
    # Get the latest test for the currently logged-in user
    latest_test = Test.objects.filter(user=request.user).order_by('-test_datetime').first()
    
    # Check if there is a test for the user
    if latest_test is None:
        # Handle the case where there is no test for the user
        return render(request, 'navagosmain/results.html', {'message': 'No test found for the current user.'})
    
    # Get the test questions and their individual results
    
    test_questions = TestQuestion.objects.filter(test = latest_test).select_related('question','chosen_answer')
        
    #Stores the questions, the chosen and the correct answer for each
    question_data = []
    
    for test_question in test_questions:
        correct_answer = QuestionAnswer.objects.filter(question=test_question.question, value=True).first()
        
        question_info = {
            'question_text': test_question.question.question_text,
            'chosen_answer': test_question.chosen_answer.answer_text if test_question.chosen_answer else 'No answer selected',
            'correct_answer': correct_answer.answer.answer_text if correct_answer else 'No correct answer'
        }
        
        question_data.append(question_info)
        
    
    
  

    context = {'latest_test': latest_test, 'question_data': question_data}
    return render(request, 'navagos_main/results.html', context)


    

    
def about(request):
    """Shows the about page"""
    return render(request, 'navagos_main/about.html')