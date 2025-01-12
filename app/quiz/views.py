from rest_framework import viewsets
from .models import Category, Question
from .serializers import CategorySerializer, QuestionSerializer


# Вьюсет для работы с категориями
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# Вьюсет для работы с вопросами
class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
