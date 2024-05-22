import random
import os
import sys

# Add the project directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'navagos.settings')
import django
django.setup()

from navagos_main.models import Question, Answer, QuestionAnswer, Category, Test


def create_test():
    random_questions = []
    categories = Category.objects.order_by("id")

    for category in categories:
        while len(random_questions) < 50:
            random_questions.extend(random.choices(Question.objects.filter(category = category), k=random.randint(1,4)))
            
            random_questions = random_questions[:50]
    
    return random_questions    

test = create_test()

print(test)


