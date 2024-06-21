from django.db import models
from django.contrib.auth.models import User

from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token


# Create your models here.


class Category(models.Model):
    category = models.TextField()

    def __str__(self):
        return self.category


class Question(models.Model):
    question_text = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None, null = True)


    def __str__(self):
        return self.question_text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, default=None)
    answer_text = models.TextField()

    def __str__(self):
        return self.answer_text


class QuestionAnswer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, default=None)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, default=None)
    value = models.BooleanField()

    def __str__(self):
        return str({
            'question': str(self.question),
            'answer': str(self.answer),
            'value': self.value
        })


class Test(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test_datetime = models.DateTimeField(auto_now_add=True)
    correct_answers = models.IntegerField() # The number of correct answers the user provided in the test.
    pass_fail = models.BooleanField()


    def __str__(self):
        test_data = f"test date: {self.test_datetime}, result: {self.correct_answers}/50 correct answers"
        return test_data


class TestQuestion(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, default=None)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, default=None)
    chosen_answer = models.ForeignKey(Answer, on_delete=models.CASCADE, default=None)
    answered_correctly = models.BooleanField()

@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)