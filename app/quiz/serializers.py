from rest_framework import serializers
from .models import Topic, Question


class QuestionSerializer(serializers.ModelSerializer):
    """Сериализатор для вопросов с краткой информацией о теме"""
    topic_name = serializers.CharField(source="topic.name", read_only=True)  # Название темы
    topic_id = serializers.IntegerField(source="topic.id", read_only=True)  # ID темы

    class Meta:
        model = Question
        fields = ["id", "text","image", "option_a", "option_b", "option_c", "option_d", "correct_answer", "topic_id", "topic_name"]


class TopicSerializer(serializers.ModelSerializer):
    """Сериализатор для темы с кратким списком вопросов"""
    difficulty_label = serializers.CharField(source="get_difficulty_display", read_only=True)  # Читаемое название сложности
    questions_count = serializers.IntegerField(source="questions.count", read_only=True)  # Количество вопросов
    questions = QuestionSerializer(many=True, read_only=True)  # Вложенные вопросы

    class Meta:
        model = Topic
        fields = ["id", "name", "description", "difficulty", "difficulty_label", "questions_count", "questions"]
