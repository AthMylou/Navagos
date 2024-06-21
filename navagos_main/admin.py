from django.contrib import admin

# Register your models here.
from .models import Answer, Question, Category, Test, QuestionAnswer, TestQuestion #User

admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Category)
admin.site.register(Test)
admin.site.register(QuestionAnswer)
admin.site.register(TestQuestion)
#admin.site.register(User)

#end of file