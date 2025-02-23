from rest_framework import serializers
from .models import Topic, Question


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"
        read_only_fields = ('create_user')


class TopicSerializer(serializers.ModelSerializer):
    """Сериализатор для темы с кратким списком вопросов"""
    difficulty_label = serializers.CharField(source="get_difficulty_display", read_only=True)  # Читаемое название сложности
    questions_count = serializers.IntegerField(source="questions.count", read_only=True)  # Количество вопросов
    questions = QuestionSerializer(many=True, read_only=True)  # Вложенные вопросы

    class Meta:
        model = Topic
        fields = ["id", "name", "description", "difficulty", "difficulty_label", "questions_count", "questions"]
