from rest_framework import serializers
from .models import Category, Question

class QuestionSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())  # Ссылка на категорию

    class Meta:
        model = Question
        fields = ['id', 'category', 'question_text', 'answer']



class CategorySerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=False)  # Включаем вопросы для каждой категории

    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'questions']

    def create(self, validated_data):
        questions_data = validated_data.pop('questions', [])
        category = Category.objects.create(**validated_data)
        for question_data in questions_data:
            Question.objects.create(category=category, **question_data)
        return category

    def update(self, instance, validated_data):
        questions_data = validated_data.pop('questions', [])
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.save()

        # Обновление или создание вопросов
        for question_data in questions_data:
            question_id = question_data.get('id', None)
            if question_id:
                question = Question.objects.get(id=question_id)
                question.question_text = question_data.get('question_text', question.question_text)
                question.answer = question_data.get('answer', question.answer)
                question.save()
            else:
                Question.objects.create(category=instance, **question_data)

        return instance

