import os
import json
import sys
from hashlib import md5

# Add the project directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'navagos.settings')
import django
django.setup()

from navagos_main.models import Category, Question, Answer, QuestionAnswer


file_path = "./questions.json"


def load_data_from_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        for item in data["questions"]:
            #create or get category
            category, created = Category.objects.get_or_create(category=item["category"])
            
            #create question
            question = Question.objects.create(question_text=item["question"], category=category)
            
            #create answers
            answers=[]
            for answer_text in item['answers']:
                answer = Answer.objects.create(question=question,answer_text=answer_text)
                answers.append(answer)
            
            # Associate correct answer with question
            correct_answer = item["correct"]
            
            
            # Set other answers as incorrect
            for answer in answers:
                answer_text = answer.answer_text
                answer_hash = md5(answer_text.encode()).hexdigest()
                if answer_hash != correct_answer:
                    QuestionAnswer.objects.create(question=question, answer=answer, value=False)
                else:
                    QuestionAnswer.objects.create(question=question, answer=answer, value=True)
                    
if __name__ == "__main__":
    json_file_path = "./questions.json"
    load_data_from_json(json_file_path)
