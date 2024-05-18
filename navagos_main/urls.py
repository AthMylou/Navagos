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
    
    path('questions/<int:question_id>/', views.question, name = 'question'),
    
    
]