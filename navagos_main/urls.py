"""Defines URL patterns for navagos_main."""

from django.urls import path
from . import views

app_name = 'navagos_main'
urlpatterns = [
    #Home page
    path('', views.index, name = 'index'),

    #Page that shows all questions
    path('questions/', views.questions, name = 'questions'),

    path('about/', views.about, name = 'about'),
    
    path('categories/', views.categories, name = 'categories'),
    
    path('categories/<int:category_id>', views.category, name = 'categoty'),
    
    path('questions/<int:question_id>/', views.question, name = 'question'),
    
    path('test/', views.test, name='test'),
    
    path('new_test/', views.new_test, name='new_test'),   
    
    path('submit_test/', views.submit_test, name = 'submit_test'),
    
    path('results/', views.results, name='results'),
]