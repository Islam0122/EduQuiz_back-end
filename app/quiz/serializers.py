from rest_framework import serializers
from .models import Category, Question


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'question_text', 'answer']


class CategorySerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)  # Включаем вопросы для каждой категории

    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'questions']
