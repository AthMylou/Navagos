from django.db import models

# Create your models here.
class User(models.Model):
    firstname = models.CharField(max_length = 100)
    lastname = models.CharField(max_length = 100)

    email = models.EmailField(max_length=200)
    passwd = models.CharField(max_length = 100)
    age = models.IntegerField(max_length = 3)

    def __str__(self):
        fullname =f"{self.firstname} {self.lastname} {self.email}" 
        return self.fullname

class Category(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None, null = True)


    def __str__(self):
        return self.question_text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, default=None)
    answer_text = models.CharField(max_length=200)

    def __str__(self):
        return self.answer_text


class QuestionAnswer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, default=None)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, default=None)
    value = models.BooleanField()


class Test(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    test_datetime = models.DateTimeField(auto_now=True)
    correct_answers = models.IntegerField() # The number of correct answers the user provided in the test.
    pass_fail = models.BooleanField()


    def __str__(self):
        test_data = f"user: {self.user}, test date: {self.test_datetime}, result: {self.correct_answers}/50 correct answers"
        return self.test_data


class TestQuestion(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, default=None)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, default=None)
    answered_correctly = models.BooleanField()

