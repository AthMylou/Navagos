from rest_framework import serializers
from navagos_main.models import *


class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = "__all__"
        
        def validate_title(self, value):
            if len(value) < 3:
                raise serializers.ValidationError("Category title must be at least 3 characters long")
            return value

class QuestionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Question
        fields = '__all__'

class AnswerSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Answer
        fields = '__all__'

class QuestionAnswerSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = QuestionAnswer
        fields = '__all__'

class TestSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Test
        fields = '__all__'

class TestQuestionSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = TestQuestion
        fields = '__all__'
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ('username', )