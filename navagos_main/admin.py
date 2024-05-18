from django.contrib import admin

# Register your models here.
from .models import Answer, Question, Category, User, Test, QuestionAnswer

admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Category)
admin.site.register(User)
admin.site.register(Test)
admin.site.register(QuestionAnswer)

#end of file